from crypt import methods
from blogposts import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from urllib import request
from blogposts.models import Blog, User
from blogposts import db
from blogposts.forms import RegisterForm, LoginForm, BlogForm
#TODO - add logging info to file when used in production
import logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # TODO - change to request check for Post
    if form.validate_on_submit():
        print("true")
        new_user = User(username=form.username.data, 
                           email=form.email.data, 
                           password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        app.logger.info(f'New user created: ', new_user)
        login_user(new_user)
        flash(f"Welcome! You are currently logged in as {new_user.username}", category="success")
        return redirect(url_for('home'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error creating user: {err_msg}', category='danger')
    return render_template('register_page.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(
            check_pwrd = form.password.data
        ):
            login_user(user)
            app.logger.info(f'user login successful:', user)
            flash(f"Login successful")
            return redirect(url_for('home'))
        else:
            flash('Incorrect email and password combination. Please try again, or register for an account', category="danger")
    print(form.errors)
    return render_template('login_page.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logout successful", category="info")
    return redirect(url_for('home'))

@app.route('/add_blog', methods=['GET','POST'])
def add_blog():
    form = BlogForm()
    print(f"Blog form: {form.__dict__}")
    if form.validate_on_submit():
        blog_post = Blog(title=form.title.data, 
                            description = form.description.data, 
                            content=form.content.data,
                            slug = form.slug.data
                            )
        #clear the form after hiting submit button
        form.title.data = ''
        form.description.data = ''
        form.content.data = ''
        form.slug.data = ''

        db.session.add(blog_post)
        db.session.commit()
        flash('Post successful')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error posting blog: {err_msg}', category='danger')
    return render_template('blog_posts.html', form = form)
   


