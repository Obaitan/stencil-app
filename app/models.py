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
    

class TemporaryPasswords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
    temp_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), index=True, nullable=False, unique=False)
    circle = db.Column(db.String(50), index=True, nullable=False, unique=False)
    zone = db.Column(db.String(20), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Name: {self.name}, {self.temp_password}>'


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, nullable=False, unique=True)
    type = db.Column(db.String(20), index=True, nullable=False, unique=False)
    link = db.Column(db.String(200), index=True, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<title: {self.title}, {self.type}>'



class Circle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    state = db.Column(db.String(20), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Circle: {self.name}>'


class Record(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    circle = db.Column(db.String(50), index=True, nullable=False, unique=False)
    zone = db.Column(db.String(20), index=True, nullable=False, unique=False)
    dob = db.Column(db.String(24), index=True, nullable=False, unique=False)
    dod = db.Column(db.String(24), index=True, nullable=False, unique=False)
    yop = db.Column(db.String(4), index=True, nullable=False, unique=False)
    cemetry = db.Column(db.String(250), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Record: {self.name}, {self.dod}>'
  

class Recent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.id)