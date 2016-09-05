# imports
from flask import redirect, render_template, request, \
    url_for, Blueprint
from flask.ext.login import login_user, \
    login_required, logout_user

from .forms import LoginForm, RegisterForm
from project import db
from project.models import Person, User, bcrypt


# config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


# routes
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(url_handle=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        new_user = User(
            url_handle=form.url_handle.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        
        new_person = Person(
            name=form.name.data,
            url_handle=form.url_handle.data,
            biography=form.biography.data,
            added_by_user_id=new_user.id
        )
        db.session.add(new_person)
        db.session.commit()

        login_user(new_user)
        return redirect('/' + new_person.url_handle)
    return render_template('register.html', form=form)
