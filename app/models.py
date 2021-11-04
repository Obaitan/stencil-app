from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, nullable=False, unique=True)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
    phone = db.Column(db.String(11), index=True, nullable=False, unique=True)
    role = db.Column(db.String(20), index=True, nullable=False, unique=False)
    password_hash = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    states = db.relationship('State', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}, {self.role}>'
    

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False, unique=True)
    zone = db.Column(db.String(10), index=True, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<State: {self.name}>'


class Recent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)