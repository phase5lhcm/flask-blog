from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, FileField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from wtforms.widgets import TextArea
from blogposts.models import User
from flask_ckeditor import CKEditorField

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
    introduction = StringField(label='Introduction', validators=[DataRequired()], widget=TextArea())
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label='Confirm password', validators=[EqualTo('password'), DataRequired()])
    submit_btn_register = SubmitField(label='Submit')

class LoginForm(FlaskForm):     
    # username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
    email = StringField(label='Email', validators=[Email(message="Email required"), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    submit_btn_login = SubmitField(label='Submit')

class BlogForm(FlaskForm):     
    title = StringField(label='Title', validators=[Length(min=2, max=20), DataRequired()])
    description = StringField("Description", validators=[Length(min=20, max=150), DataRequired()])
    # author = StringField(label='Email', validators=[Email(message="Email required"), DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])   
    submit_btn_blog = SubmitField(label='Post blog')
    feature_img = FileField("Image")

class ImageForm(FlaskForm):     
    name = StringField(label='Title', validators=[ DataRequired()])
    submit_btn_img = SubmitField(label='Submit')

class SearchForm(FlaskForm):     
    searched = StringField(label='Searched', validators=[ DataRequired()])
    submit_btn_search = SubmitField(label='Submit')

