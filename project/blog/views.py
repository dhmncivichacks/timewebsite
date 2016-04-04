# imports
from flask import render_template, Blueprint

from project import db   # pragma: no cover
from project.models import Blog   # pragma: no cover
from project.models import BlogPost   # pragma: no cover


# config
blog_blueprint = Blueprint(
    'blog', __name__,
    template_folder='templates'
)   # pragma: no cover


# routes
@blog_blueprint.route('/blog', methods=['GET', 'POST'])   # pragma: no cover
def blog():
    error = None
    posts = db.session.query(BlogPost).all()
    return render_template(
        'blog.html', posts=posts, error=error)
