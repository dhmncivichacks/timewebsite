from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class PersonForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    url_handle = TextField('Url handle', validators=[DataRequired()])
    biography = TextField('Biography', validators=[DataRequired()])
