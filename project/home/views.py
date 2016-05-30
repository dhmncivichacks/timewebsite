
# imports
from flask import render_template, Blueprint   # pragma: no cover

from project import db   # pragma: no cover
from project.models import Person   # pragma: no cover

import random


# config
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover
MAX_GRID_SIZE_HOMEPAGE_PEOPLE = 6


# routes
# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    error = None
    current_person_count = db.session.query(Person).count()
    if current_person_count <= MAX_GRID_SIZE_HOMEPAGE_PEOPLE:
        persons = db.session.query(Person).all()
    else:
        persons = []
        while len(persons) < MAX_GRID_SIZE_HOMEPAGE_PEOPLE:
            rand = random.randrange(0, current_person_count)
            random_person = db.session.query(Person)[rand]
            if random_person not in persons:
                persons.append(random_person)
    return render_template(
        'index.html', persons=persons, error=error)
