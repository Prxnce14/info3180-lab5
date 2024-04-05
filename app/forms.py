# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=255)])
    poster = FileField('Movie Poster', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPEG, JPG, and PNG images are allowed!')
    ])

