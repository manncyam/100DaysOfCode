# Day64 List Top Favorite Movies Website

## Libraries

- Flask
- WTForms
- SQList
- [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)

## How to turn results to python list

```python
results = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
movies = results.all()
```
