# imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os

# config
app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.url_map.strict_slashes = False  # handle /foo and /foo/
db = SQLAlchemy(app)

from project.dynamic_routes.views import dynamic_routes_blueprint
from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.blog.views import blog_blueprint
from project.people.views import people_blueprint
from project.organizations.views import organizations_blueprint
from project.events.views import events_blueprint

# register our blueprints
app.register_blueprint(dynamic_routes_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(people_blueprint)
app.register_blueprint(organizations_blueprint)
app.register_blueprint(events_blueprint)

from project.models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
