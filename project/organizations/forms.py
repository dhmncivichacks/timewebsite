from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class OrganizationForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    url_handle = TextField('Url handle', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
