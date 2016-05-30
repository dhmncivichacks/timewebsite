# imports
from flask import request  # pragma: no cover
from flask import render_template  # pragma: no cover
from flask import Blueprint  # pragma: no cover
from flask import redirect  # pragma: no cover
from flask import url_for  # pragma: no cover

from flask.ext.login import current_user  # pragma: no cover

from project import db  # pragma: no cover
from project.models import Person  # pragma: no cover

from .forms import PersonForm  # pragma: no cover


# config
people_blueprint = Blueprint(
    'people', __name__,
    template_folder='templates'
)   # pragma: no cover


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
                added_by_id=current_user.id
            )
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('people.people'))
        else:
            error = 'FIXME ERROR'
    people = db.session.query(Person).all()
    return render_template(
        'people.html', form=form, people=people, error=error)
