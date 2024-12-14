from . import db
from flask_sqlalchemy import SQLAlchemy


# creating a model class for users
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 

    def __repr__(self): 
        return '<User %r>' % self.id
    
# convert to dictionary it mens to json,object api
    def to_dict(self):
        return{
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email
        }

