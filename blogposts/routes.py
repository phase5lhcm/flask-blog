from flask import Flask, render_template
from blogposts import app

@app.route("/")
def hello_world():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template('login_page.html')