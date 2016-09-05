from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class EventForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
