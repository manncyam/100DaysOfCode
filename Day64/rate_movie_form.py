from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import NumberRange, DataRequired, InputRequired

class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10. e.g 7.5', validators=[NumberRange(min=0, max=10), InputRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    update = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')