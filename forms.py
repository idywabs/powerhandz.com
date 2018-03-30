from wtforms import Form, TextField, TextAreaField, SubmitField
from wtforms.validators import Email, InputRequired, Optional, URL, ValidationError

class ContactForm(Form):
  name = TextField("Name", [InputRequired("Please enter your name.")])
  email = TextField("Email",  [InputRequired("Please enter your email address."), Email("Please enter a valid email address.")])
  name = TextField("Company")
  name = TextField("Website", [Optional(), URL("Please enter your name.")])
  message = TextAreaField("Message", [InputRequired("Please enter a message.")])
  submit = SubmitField("Send")
