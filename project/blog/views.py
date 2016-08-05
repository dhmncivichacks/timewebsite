# imports
from flask import request
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

from flask.ext.login import current_user

from project import db
from project.models import BlogPost

from .forms import BlogPostForm


# config
blog_blueprint = Blueprint(
    'blog', __name__,
    template_folder='templates'
) 


# routes
@blog_blueprint.route('/blog', methods=['GET', 'POST'])
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
