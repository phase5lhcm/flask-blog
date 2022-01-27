from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from wtforms.widgets import TextArea
from blogposts.models import User

class RegisterForm(FlaskForm):
    
    def validate_username(self, check_username):
        #query documents to see if user already exists in db with this username
        user = User.query.filter_by(username=check_username.data).first()
        if user:
            raise ValidationError('Username already exists.')
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email: 
            raise ValidationError('Email addrress already exists, please log in with your account.')
        
    username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
    email = StringField(label='Email', validators=[Email(message="Email required"), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label='Confirm password', validators=[EqualTo('password'), DataRequired()])
    submit_btn_register = SubmitField(label='Create Account')

class LoginForm(FlaskForm):     
    # username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
    email = StringField(label='Email', validators=[Email(message="Email required"), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    submit_btn_login = SubmitField(label='Submit')

class BlogForm(FlaskForm):     
    title = StringField(label='Title', validators=[Length(min=2, max=20), DataRequired()])
    description = StringField("Description", validators=[Length(min=20, max=150), DataRequired()])
    # author = StringField(label='Email', validators=[Email(message="Email required"), DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    slug = StringField("Slug", validators=[DataRequired()])
    submit_btn_blog = SubmitField(label='Post blog')

