from project import db
from project.models import Blog
from project.models import BlogPost
from project.models import Event
from project.models import Person
from project.models import Organization
from project.models import NewsItem
from project.models import Sponsor
from project.models import User

# create the database and the db tables
db.create_all()
db.session.commit()

# initial user
db.session.add(User(email="ad@min.com", password="admin", url_handle="admin"))
db.session.commit()