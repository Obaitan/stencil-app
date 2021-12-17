from enum import unique
from operator import index
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
    phone = db.Column(db.String(14), index=True, nullable=False, unique=True)
    role = db.Column(db.String(20), index=True, nullable=False, unique=False)
    circle = db.Column(db.String(50), index=True, nullable=False, unique=False)
    zone = db.Column(db.String(20), index=True, nullable=False, unique=False)
    password_hash = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # circle = db.relationship('Circle', backref='person', lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.name}, {self.role}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True, nullable=False, unique=True)
    file_type = db.Column(db.String(20), index=True, nullable=False, unique=False)
    link = db.Column(db.String(200), index=True, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<title: {self.title}, {self.file_type}>'



class Circle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    state = db.Column(db.String(20), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Circle: {self.name}>'


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=False)
    circle = db.Column(db.String(50), index=True, nullable=False, unique=False)
    zone = db.Column(db.String(20), index=True, nullable=False, unique=False)
    dob = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    dod = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    yop = db.Column(db.DateTime, index=True, nullable=True, unique=False)
    cemetry = db.Column(db.String(250), index=True, nullable=True, unique=False)
    status = db.Column(db.String(250), index=True, nullable=False, unique=False, default="Processing")
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Record: {self.name}, {self.dod}>'


class LoginRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=False)
    role = db.Column(db.String(20), index=True, nullable=False, unique=False)
    zone = db.Column(db.String(20), index=True, nullable=False, unique=False)
    status = db.Column(db.String(7), index=True, nullable=False, unique=False)
    last_seen = db.Column(db.DateTime, index=True, nullable=False, unique=False)

    def __repr__(self):
        return f'<User: {self.name}, {self.role}>'
  
  
class Stencil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, nullable=False, unique=True)
    date = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    file = db.Column(db.LargeBinary, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Stencil: {self.title}>'


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), index=True, nullable=False, unique=True)
    data = db.Column(db.LargeBinary, nullable=False)
    width = db.Column(db.String(2), index=True, nullable=False, unique=False)
    height = db.Column(db.String(2), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Character: {self.name}>'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), index=True, nullable=False, unique=True)
    date = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    file = db.Column(db.LargeBinary, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Report: {self.title}>'


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, nullable=False, unique=False)
    message = db.Column(db.Text, index=True, nullable=False, unique=True)
    date = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    status = db.Column(db.String(7), index=True, nullable=False, unique=False, default="Unread")
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    