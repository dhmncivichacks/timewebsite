from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    name = StringField(
        'name',
        validators=[DataRequired(), Length(min=3, max=50)]
    )
    biography = StringField(
        'biography',
        validators=[DataRequired(), Length(min=1, max=256)]
    )
    url_handle = StringField(
        'url_handle',
        validators=[DataRequired(), Length(min=3, max=256)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
