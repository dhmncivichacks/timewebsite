from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class EventForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
