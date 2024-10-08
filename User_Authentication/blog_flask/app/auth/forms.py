# Modules
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, Length
from flask_wtf import FlaskForm
from ..models import User

# Classes

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),
                        Length(1,64),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In') 

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(3,10),
                                                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Username must have only letters')])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password2',message='Passwords must match')])
    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def validate_email(self, field:str) -> ValidationError:
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Useraname already in use')
    
    def validate_username(self, field:str) -> ValidationError:
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password',validators=[DataRequired()])
    password = PasswordField('New password',validators=[DataRequired(),
                                                        EqualTo('password2',message='Password must match')])
    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    submit = SubmitField('Reset Password')

class PasswordResetForm(FlaskForm):
    password = PasswordField('New password',validators=[DataRequired(),EqualTo('password2',message='Password must match')])
    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Reset Password')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Update Email Address')
    
    def validate_email(self,field:str) -> ValidationError:
        if (User.query.filter_by(email=field.data.lower())).first():
            raise ValidationError('Email already registered')