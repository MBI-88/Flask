# Script to create formulary set

# Modules
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, TextAreaField, SubmitField

# Classes

class User(FlaskForm):
    name = StringField(label = 'Name',validators = [DataRequired(),Length(min = 8, max = 15)])
    text = TextAreaField(label = 'Text',validators = [DataRequired()])
    send = SubmitField(label = 'Send')
