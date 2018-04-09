# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import FormField, HiddenField, IntegerField, TextField, TextAreaField, RadioField, SelectField, SubmitField, validators
from wtforms.validators import Email, InputRequired, Optional, URL, ValidationError

class AddressForm(Form):
    country = SelectField(
            'Country',
            [
                InputRequired('Please select a country.'),
            ],
            choices= [
                    'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa',
                    'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
                    'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
                    'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                    'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                    'Bonaire, Saint Eustatius and Saba', 'Bosnia and Herzegovina',
                    'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
                    'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
                    'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
                    'Central African Republic', 'Chad', 'Chile', 'China',
                    'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros',
                    'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands',
                    'Costa Rica', 'Cote D\'ivoire', 'Croatia', 'Curaçao', 'Cyprus',
                    'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
                    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
                    'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland',
                    'France', 'French Guiana', 'French Polynesia',
                    'French Southern Territories', 'Gabon', 'Gambia, The', 'Georgia',
                    'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada',
                    'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
                    'Guinea-Bissau', 'Guyana', 'Haiti',
                    'Heard Island and the McDonald Islands', 'Holy See', 'Honduras',
                    'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq',
                    'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
                    'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
                    'Korea, Republic of', 'Kosovo', 'Kuwait', 'Kyrgyzstan',
                    'Lao People\'s Democratic Republic', 'Latvia', 'Lebanon', 'Lesotho',
                    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
                    'Macedonia, The Former Yugoslav Republic of', 'Madagascar', 'Malawi',
                    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
                    'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
                    'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco',
                    'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
                    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
                    'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua',
                    'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
                    'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
                    'Palestinian Territories', 'Panama', 'Papua New Guinea', 'Paraguay',
                    'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico',
                    'Qatar', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda',
                    'Saint Barthelemy', 'Saint Helena, Ascension and Tristan da Cunha',
                    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin',
                    'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines',
                    'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                    'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
                    'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
                    'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain',
                    'Sri Lanka', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland',
                    'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan',
                    'Tanzania, United Republic of', 'Thailand', 'Timor-leste', 'Togo',
                    'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                    'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda',
                    'Ukraine', 'United Arab Emirates', 'United Kingdom',
                    'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan',
                    'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands, British',
                    'Virgin Islands, U.S.', 'Wallis and Futuna', 'Western Sahara', 'Yemen',
                    'Zambia', 'Zimbabwe'],
            render_kw={'placeholder': 'Address *'})
    address_line_1 = TextField(
            'Street Address',
            [
                InputRequired('Please enter your address.'),
            ],
            render_kw={'placeholder': 'Address *'})
    address_line_2 = TextField(
            'Street Address Line 2',
            render_kw={'placeholder': 'Apartment, suite, unit, building, floor, etc.'})
    city = TextField(
            'City',
            [
                InputRequired('Please enter your city.'),
            ],
            render_kw={'placeholder': 'City *'})
    state = TextField(
            'State',
            [
                InputRequired('Please enter your state, province, or region.'),
            ],
            render_kw={'placeholder': 'State / Province / Region *'})
    zip_code = TextField(
            'Zip Code',
            [
                InputRequired('Please enter your zip code.'),
            ],
            render_kw={'placeholder': 'Zip Code *'})


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

class ReturnForm(Form):
    first_name = TextField(
            'First Name',
            [
                InputRequired('Please enter your first name.')
            ],
            render_kw={'placeholder': 'First Name *'})
    last_name = TextField(
            'Last Name',
            [
                InputRequired('Please enter your last name.')
            ],
            render_kw={'placeholder': 'Last Name *'})
    email = TextField(
            'Email',
            [
                InputRequired('Please enter your email address.'),
                Email('Please enter a valid email address.')
            ],
            render_kw={'placeholder': 'Email Address *'})
    phone_number = TextField(
            'Phone Number',
            [
                InputRequired('Please enter your email address.'),
                Email('Please enter a valid email address.')
            ],
            render_kw={'placeholder': 'Phone Number *'})
    order_number = IntegerField(
            'Order Number',
            [
                InputRequired('Please enter your order number.')
            ],
            render_kw={'placeholder': 'Order Number *'})
    address = FormField(AddressForm)
    submit = SubmitField('Send')

