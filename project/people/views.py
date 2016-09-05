# imports
from flask import request
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

from flask.ext.login import current_user

from project import db
from project.models import Person

from .forms import PersonForm


# config
people_blueprint = Blueprint(
    'people', __name__,
    template_folder='templates'
) 


# routes
@people_blueprint.route('/people', methods=['GET', 'POST'])
def people():
    error = None
    form = PersonForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_person = Person(
                name=form.name.data,
                url_handle=form.url_handle.data,
                biography=form.biography.data,
                added_by_user_id=current_user.id
            )
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('people.people'))
        else:
            error = 'FIXME ERROR'
    people = db.session.query(Person).all()
    return render_template(
        'people.html', form=form, people=people, error=error)
