
# imports
from flask import render_template, Blueprint

from project import db   # pragma: no cover
from project.models import BlogPost   # pragma: no cover


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
    posts = db.session.query(BlogPost).all()
    return render_template(
        'index.html', posts=posts, error=error)
