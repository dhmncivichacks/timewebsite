
# imports
from flask import render_template, Blueprint

from flask import current_app

from project import db   # pragma: no cover
from project.models import Person   # pragma: no cover


# config
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


# routes
# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])   # pragma: no cover
def home():
    error = None
    persons = db.session.query(Person).all()
    current_app.logger.debug(persons)
    return render_template(
        'index.html', persons=persons, error=error)
