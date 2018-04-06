from flask_wtf import FlaskForm as Form
from wtforms import HiddenField, TextField, TextAreaField, SubmitField, validators
from wtforms.validators import Email, InputRequired, Optional, URL, ValidationError

class ContactForm(Form):
  name = TextField('Name', [InputRequired('Please enter your name.')], render_kw={'placeholder': 'Full Name *'})
  email = TextField('Email',  [InputRequired('Please enter your email address.'), Email('Please enter a valid email address.')], render_kw={'placeholder': 'Email Address *'})
  company = TextField('Company', render_kw={'placeholder': 'Company / Organization'})
  website = TextField('Website', [Optional(), URL('Please enter a valid URL.')], render_kw={'placeholder': 'Website'})
  message = TextAreaField('Message', [InputRequired('Please enter a message.')], render_kw={'placeholder': 'Message'})
  submit = SubmitField('Send', render_kw={'class': 'button btnBlack float-right'})
