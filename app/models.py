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
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import email_validator



class registrationForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(), validators.Length(min=6),
        validators.EqualTo('confirm', message='Password mismatch!')
    ])
    #file = FileField('File')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #The submit button was of no effect inserting data into the table
    #submit = SubmitField('Complete Registeration')

class uploadForm(Form):
    #docname = StringField( validators=[Required()])
    phonenum = StringField('Mobile Number', [validators.Length(min=10, max=11)])
    emailadd = StringField('Email Address', [validators.Email()])
    docfile = FileField()
    pass
    
class loginForm(Form):
    username = StringField( validators=[Required()])
    password = PasswordField( validators=[Required()])

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
