from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename
import uuid as uuid
from flask_moment import Moment
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogposts.db'
app.config['SECRET_KEY'] = b'u>$\x8b\xd7\x1e\x1a\xcf\xa8k\xa3\x14'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
moment = Moment(app)

from blogposts import routes