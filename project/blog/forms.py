from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class BlogPostForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    body = TextField('Body', validators=[DataRequired()])
