from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
all_books = []


db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement='auto')
    title: Mapped[str] = mapped_column(db.String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(db.String(250), nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars()
        
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        with app.app_context():
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add.html')

@app.route('/edit/id=<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = db.get_or_404(Book, id)
    if request.method == 'GET':
        return render_template('edit.html', book=book)
    book.rating = float(request.form['rating'])
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

