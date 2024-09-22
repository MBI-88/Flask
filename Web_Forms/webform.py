# Script to make Form class

# Modules
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo
from flask_wtf import FlaskForm


# Classes
class MyForm(FlaskForm):
    name = StringField( "Name",validators=[DataRequired(),Length(min=10,max=15)])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=4,max=8),])
    confirm = PasswordField("Repeat password",validators=[DataRequired(),Length(min=4,max=8),
                            EqualTo('password',message='Password must match')])
    submit = SubmitField('Sumbit')
    
    







