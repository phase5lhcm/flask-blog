from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from blogposts import db, login_manager
from blogposts import bcrypt
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text(), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    author_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    slug = db.Column(db.String(20))
    # featured_img = db.Column(db.String,nullable=False)
    # author = db.relationship('User', backref=db.backref('user',lazy=True))

    def __repr__(self):
        return '<Blog Post Title %r>' % self.title




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=8),nullable=False)
    free_posts = db.Column(db.Integer(), nullable=False,default=5)
    blog_posts = db.relationship('Blog', backref='blog_author', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password): 
        #let's override what is stored in password_hash field
         self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
         return True

