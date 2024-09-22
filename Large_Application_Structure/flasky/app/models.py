# Script to make Database models

# Modules
from . import db

# Models
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship('User',backref = 'role') # Relation to User / use lazy='dynamic' (it dont use query)

    def __repr__(self) -> str:
        return '<Role %r>'% self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self) -> str:
        return '<User %r>'% self.username