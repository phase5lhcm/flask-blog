from blogposts import app
from flask import render_template
from blogposts.models import Blog
from blogposts.forms import RegisterForm

@app.route("/")
def hello_world():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template('login_page.html')

@app.route("/register")
def register():
    form = RegisterForm()
    return render_template('register_page.html', form=form)