from project import db
from project import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Blog(db.Model):

    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)

    def __init__(self, title, url_handle):
        self.title = title
        self.url_handle = url_handle

    def __repr__(self):
        return '<title - {}>'.format(self.title)


class BlogPost(db.Model):

    __tablename__ = "blogposts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))
    url_handle = db.Column(db.String, nullable=False)

    def __init__(self, title, body, author_id, url_handle):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.url_handle = url_handle

    def __repr__(self):
        return '<title {}'.format(self.title)


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, url_handle, description):
        self.description = description
        self.title = title
        self.url_handle = url_handle

    def __repr__(self):
        return '<title - {}>'.format(self.title)


class Person(db.Model):

    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)
    biography = db.Column(db.String, nullable=False)
    added_by_user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, name, url_handle, biography, added_by_user_id):
        self.name = name
        self.url_handle = url_handle
        self.biography = biography
        self.added_by_user_id = added_by_user_id


class Organization(db.Model):

    __tablename__ = "organizations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name, description, url_handle):
        self.name = name
        self.description = description
        self.url_handle = url_handle

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class NewsItem(db.Model):

    __tablename__ = "newsitems"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)

    def __init__(self, title, url_handle):
        self.title = title
        self.url_handle = url_handle

    def __repr__(self):
        return '<title - {}>'.format(self.title)


class Sponsor(db.Model):

    __tablename__ = "sponsors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url_handle = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name, url_handle, description):
        self.name = name
        self.description = description
        self.url_handle = url_handle

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    posts = relationship("BlogPost", backref="author")
    url_handle = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password, url_handle):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.url_handle = url_handle

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
