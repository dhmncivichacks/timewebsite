# imports
from flask import request
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

from flask.ext.login import current_user

from project import db
from project.models import Event

from .forms import EventForm


# config
events_blueprint = Blueprint(
    'events', __name__,
    template_folder='templates'
) 


# routes
@events_blueprint.route('/events', methods=['GET', 'POST'])
def events():
    error = None
    form = EventForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_event = Event(
                title = form.title.data,
                description = form.description.data,
                url_handle = 'a_url_handle_for_this_event'  # FIXME
            )
            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('events.events'))
        else:
            error = 'FIXME ERROR'
    events = db.session.query(Event).all()
    return render_template(
        'events.html', form=form, events=events, error=error)
