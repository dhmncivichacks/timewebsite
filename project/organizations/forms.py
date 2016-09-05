from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class OrganizationForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    url_handle = StringField('Url handle', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
