from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class PersonForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    url_handle = StringField('Url handle', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])
