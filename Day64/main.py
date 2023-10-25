from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import requests
from movie_db import db, Movie
from rate_movie_form import RateMovieForm, AddMovieForm
import os

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

Bootstrap5(app)

db.init_app(app)

with app.app_context():
    db.create_all()

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

# if True:
#     with app.app_context():
#         db.drop_all()

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ['movid_db_api']}"
}

@app.route("/")
def home():
    results = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    movies = results.all()
    count = len(movies)
    
    for i in range(count):
        movies[i].ranking = count - i
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    rate_form = RateMovieForm()
    with app.app_context():
        id = request.args.get('id')
        movie = db.get_or_404(Movie, id)

        if rate_form.validate_on_submit():
            movie.rating = rate_form.rating.data
            movie.review = rate_form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        
        return render_template('edit.html', movie=movie, form=rate_form)

@app.route('/delete/<int:id>')
def delete(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))    

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        url = f"https://api.themoviedb.org/3/search/movie?query={form.title.data}&include_adult=false&language=en-US&page=1"
        response = requests.get(url, headers=headers)

        results = response.json()['results']

        return render_template('select.html', results=results)
    
    return render_template('add.html', form=form)

@app.route('/find', methods=['GET', 'POST'])
def find():
    id = request.args.get('id')
    if id is not None:
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()
        movie = Movie(
            title=data['title'],
            year=int(data['release_date'].split('-')[0]),
            description=data['overview'],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('edit', id=movie.id))
        
if __name__ == '__main__':
    app.run(debug=True)
