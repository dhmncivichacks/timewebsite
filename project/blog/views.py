# imports
from flask import request # pragma: no cover
from flask import render_template # pragma: no cover
from flask import Blueprint # pragma: no cover
from flask import redirect # pragma: no cover
from flask import url_for # pragma: no cover

from flask.ext.login import current_user # pragma: no cover

from project import db   # pragma: no cover
from project.models import BlogPost   # pragma: no cover

from .forms import BlogPostForm # pragma: no cover


# config
blog_blueprint = Blueprint(
    'blog', __name__,
    template_folder='templates'
)   # pragma: no cover


# routes
@blog_blueprint.route('/blog', methods=['GET', 'POST']) # pragma: no cover
def blog():
    error = None
    form = BlogPostForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_blogpost = BlogPost(
                form.title.data,
                form.body.data,
                current_user.id,
                'a_url_handle_for_this_blog_post'  # FIXME
            )
            db.session.add(new_blogpost)
            db.session.commit()
            return redirect(url_for('blog.blog'))
        else:
            error = 'FIXME ERROR'
    posts = db.session.query(BlogPost).all()
    return render_template(
        'blog.html', form=form, posts=posts, error=error)
