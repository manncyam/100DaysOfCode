from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '4e9acce7d4b389ee0391a0f5bb5d70745243edca6f5896acc0aa5df50756e6fa944c3ac52b109c4eae2757713698fec4098c654c2a1b32e25a96242de3342016'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Flask login
login_manager = LoginManager()
login_manager.init_app(app)

app.config['DOWNLOAD_FOLDER'] = './static/files/'

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one_or_none()
    return user

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar_one_or_none()
        if user == None:
            password = request.form.get('password')
            hash_password = generate_password_hash(password, salt_length=8)
            user = User(
                email = request.form.get('email'),
                password = hash_password,
                name = request.form.get('name')
            )
            with app.app_context(): 
                db.session.add(user)
                db.session.commit()
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
        else:
            flash('You already sign up with the email. Using Login instead!')
            return redirect(url_for('register'))
        
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar_one_or_none()
        if user == None:
            flash("You are not registered yet.")
            return redirect(url_for('login'))
        if check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets', name=user.name))
        else:
            flash("Wrong Username or Password.")
            return redirect(url_for('login'))
    
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=request.args.get('name'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download/<path:name>')
@login_required
def download(name):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], name)


if __name__ == "__main__":
    app.run(debug=True)
