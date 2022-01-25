from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from blogposts import db 
from datetime import date, datetime

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.Text(), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('user',lazy=True))

    def __repr__(self):
        return '<Blog Post Title %r>' % self.title


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username