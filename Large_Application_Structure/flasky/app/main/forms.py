# Script to make formulary

# Modules
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

#Formulay Class
class MyForm(FlaskForm):
    name = StringField(label = 'Name', validators = [DataRequired(), 
                        Length(5, 15, message = 'Name most be between 5 and 15 characters')])
    password = PasswordField(label = 'Password', validators = [DataRequired(), 
                             Length(4, 8, message = 'Password most be between 4 and 8 characters')])
    role = StringField(label = 'Role', validators = [DataRequired(),
                        Length(4, 5, message = 'Required Admin or User')])
    submited = SubmitField(label = 'Submit')
    