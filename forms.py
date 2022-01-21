from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import DataRequired
class PredictionForm(FlaskForm):
  image = FileField('file', validators=[
    DataRequired()
  ])
  submit = SubmitField('Submit')