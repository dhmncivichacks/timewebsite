from flask import render_template, Blueprint, abort
from project.models import Event
from project.models import Organization
from project.models import Person


dynamic_routes_blueprint = Blueprint(
    'dynamic_routes', __name__,
    template_folder='templates'
)


# Dynamic router for nice urls example.com/billgates or example.com/barcampgb
@dynamic_routes_blueprint.route('/<path:path>')
def dynamic_routes(path):

    event = Event.query.filter_by(url_handle=path).first()
    organization = Organization.query.filter_by(url_handle=path).first()
    person = Person.query.filter_by(url_handle=path).first()

    if person:
        return render_template('person.html', person=person)
    elif event:
        return render_template('event.html', event=event)
    elif organization:
        return render_template('organization.html', organization=organization)
    else:
        return abort(404)
