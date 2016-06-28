# imports
from flask import request  # pragma: no cover
from flask import render_template  # pragma: no cover
from flask import Blueprint  # pragma: no cover
from flask import redirect  # pragma: no cover
from flask import url_for  # pragma: no cover

from project import db  # pragma: no cover
from project.models import Organization  # pragma: no cover

from .forms import OrganizationForm  # pragma: no cover


# config
organizations_blueprint = Blueprint(
    'organizations', __name__,
    template_folder='templates'
)   # pragma: no cover


# routes
@organizations_blueprint.route('/organizations', methods=['GET', 'POST'])
def organizations():
    error = None
    form = OrganizationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_organization = Organization(
                name=form.name.data,
                url_handle=form.url_handle.data,
                description=form.description.data,
            )
            db.session.add(new_organization)
            db.session.commit()
            return redirect(url_for('organizations.organizations'))
        else:
            error = 'FIXME ERROR'
    organizations = db.session.query(Organization).all()
    return render_template(
        'organizations.html',
        form=form,
        organizations=organizations,
        error=error)
