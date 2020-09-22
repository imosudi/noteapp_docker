#import virtualenv python library directory
import os
import sys
#sys.path.insert(0, '/venv/lib/python(/site-packages')

#Import from noteapp.py
#from noteapp import db


#import installed library
from flask_wtf import FlaskForm

from wtforms import Form, StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required
from wtforms.widgets import TextArea
#from flask_wtf.file import FileField



class registrationForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    #file = FileField('File')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #The submit button was of no effect inserting data into the table
    #submit = SubmitField('Complete Registeration')


class loginForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Login Password', validators=[Required()])

class createNoteForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=12)])
    body = StringField(u'Take a note', widget=TextArea())
    username = HiddenField('username')
#CREATE TABLE notes(id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(14), body VARCHAR(270), create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

class editNoteForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=12)])
    body = StringField(u'Take a note', widget=TextArea())
    author = HiddenField('author')

class deleteNoteForm(Form):
    note_id = HiddenField('note_id')

class preEditNoteForm(Form):
    note_id = HiddenField('note_id')
