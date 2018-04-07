from flask_wtf import FlaskForm as Form
from wtforms import HiddenField, TextField, TextAreaField, RadioField, SubmitField, validators
from wtforms.validators import Email, InputRequired, Optional, URL, ValidationError

class ContactForm(Form):
    name = TextField(
            'Name',
            [
                InputRequired('Please enter your name.')
            ],
            render_kw={'placeholder': 'Full Name *'})
    email = TextField(
            'Email',
            [
                InputRequired('Please enter your email address.'),
                Email('Please enter a valid email address.')
            ],
            render_kw={'placeholder': 'Email Address *'})
    company = TextField(
            'Company',
            render_kw={'placeholder': 'Company'})
    website = TextField(
            'Website',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'Website'})
    message = TextAreaField(
            'Message',
            [
                InputRequired('Please enter a message.')
            ],
            render_kw={'placeholder': 'Message *'})
    submit = SubmitField('Send')

class AffiliateApplication(Form):
    name = TextField(
            'Name',
            [
                InputRequired('Please enter your name.')
            ],
            render_kw={'placeholder': 'Full Name *'})
    email = TextField(
            'Email',
            [
                InputRequired('Please enter your email address.'),
                Email('Please enter a valid email address.')
            ],
            render_kw={'placeholder': 'Email Address *'})
    company = TextField(
            'Company',
            render_kw={'placeholder': 'Company'})
    website = TextField(
            'Website',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'Website'})
    facebook = TextField(
            'Facebook',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'Facebook'})
    instagram = TextField(
            'Instagram',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'Instagram'})
    twitter = TextField(
            'Twitter',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'Twitter'})
    youtube = TextField(
            'YouTube',
            [
                Optional(),
                URL('Please enter a valid URL.')
            ],
            render_kw={'placeholder': 'YouTube'})
    provides_training = RadioField(
            'Do you provide sport performance training? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    hosts_yearly_clinics = RadioField(
            'Do you host training clinics throughout the year? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    provides_video_content = RadioField(
            'Do you provide video content for social media platforms? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    trains_professional_athletes  = RadioField(
            'Do you train professional athletes? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    sells_merchandise = RadioField(
            'Do you currently sell merchandise on your website? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    has_blog = RadioField(
            'Do you have a blog or newsletter database? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
    submit = SubmitField('Apply')

