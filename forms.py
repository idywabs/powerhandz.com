# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, FileField, FormField, HiddenField, IntegerField, TextField, TextAreaField, RadioField, SelectField, SelectMultipleField, SubmitField, validators
from wtforms.validators import Email, InputRequired, Optional, URL, ValidationError

class AddressForm(Form):
    class Meta:
        csrf = False

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
    country = SelectField(
            'Country',
            [
                InputRequired('Please select a country.'),
            ],
            choices=[
                    (u'Afghanistan', u'Afghanistan'),
                    (u'Aland Islands', u'Aland Islands'),
                    (u'Albania', u'Albania'),
                    (u'Algeria', u'Algeria'),
                    (u'American Samoa', u'American Samoa'),
                    (u'Andorra', u'Andorra'),
                    (u'Angola', u'Angola'),
                    (u'Anguilla', u'Anguilla'),
                    (u'Antarctica', u'Antarctica'),
                    (u'Antigua and Barbuda', u'Antigua and Barbuda'),
                    (u'Argentina', u'Argentina'),
                    (u'Armenia', u'Armenia'),
                    (u'Aruba', u'Aruba'),
                    (u'Australia', u'Australia'),
                    (u'Austria', u'Austria'),
                    (u'Azerbaijan', u'Azerbaijan'),
                    (u'Bahamas, The', 'Bahamas, The'),
                    (u'Bahrain', u'Bahrain'),
                    (u'Bangladesh', u'Bangladesh'),
                    (u'Barbados', u'Barbados'),
                    (u'Belarus', u'Belarus'),
                    (u'Belgium', u'Belgium'),
                    (u'Belize', u'Belize'),
                    (u'Benin', u'Benin'),
                    (u'Bermuda', u'Bermuda'),
                    (u'Bhutan', u'Bhutan'),
                    (u'Bolivia', u'Bolivia'),
                    (u'Bonaire, Saint Eustatius and Saba', 'Bonaire, Saint Eustatius and Saba'),
                    (u'Bosnia and Herzegovina', u'Bosnia and Herzegovina'),
                    (u'Botswana', u'Botswana'),
                    (u'Bouvet Island', u'Bouvet Island'),
                    (u'Brazil', u'Brazil'),
                    (u'British Indian Ocean Territory', u'British Indian Ocean Territory'),
                    (u'Brunei Darussalam', u'Brunei Darussalam'),
                    (u'Bulgaria', u'Bulgaria'),
                    (u'Burkina Faso', u'Burkina Faso'),
                    (u'Burundi', u'Burundi'),
                    (u'Cambodia', u'Cambodia'),
                    (u'Cameroon', u'Cameroon'),
                    (u'Canada', u'Canada'),
                    (u'Cape Verde', u'Cape Verde'),
                    (u'Cayman Islands', u'Cayman Islands'),
                    (u'Central African Republic', u'Central African Republic'),
                    (u'Chad', u'Chad'),
                    (u'Chile', u'Chile'),
                    (u'China', u'China'),
                    (u'Christmas Island', u'Christmas Island'),
                    (u'Cocos (Keeling) Islands', u'Cocos (Keeling) Islands'),
                    (u'Colombia', u'Colombia'),
                    (u'Comoros', u'Comoros'),
                    (u'Congo', u'Congo'),
                    (u'Congo, The Democratic Republic of the', 'Congo, The Democratic Republic of the'),
                    (u'Cook Islands', u'Cook Islands'),
                    (u'Costa Rica', u'Costa Rica'),
                    (u'Cote D\'ivoire', u'Cote D\'ivoire'),
                    (u'Croatia', u'Croatia'),
                    (u'Curaçao', u'Curaçao'),
                    (u'Cyprus', u'Cyprus'),
                    (u'Czech Republic', u'Czech Republic'),
                    (u'Denmark', u'Denmark'),
                    (u'Djibouti', u'Djibouti'),
                    (u'Dominica', u'Dominica'),
                    (u'Dominican Republic', u'Dominican Republic'),
                    (u'Ecuador', u'Ecuador'),
                    (u'Egypt', u'Egypt'),
                    (u'El Salvador', u'El Salvador'),
                    (u'Equatorial Guinea', u'Equatorial Guinea'),
                    (u'Eritrea', u'Eritrea'),
                    (u'Estonia', u'Estonia'),
                    (u'Ethiopia', u'Ethiopia'),
                    (u'Falkland Islands (Malvinas)', u'Falkland Islands (Malvinas)'),
                    (u'Faroe Islands', u'Faroe Islands'),
                    (u'Fiji', u'Fiji'),
                    (u'Finland', u'Finland'),
                    (u'France', u'France'),
                    (u'French Guiana', u'French Guiana'),
                    (u'French Polynesia', u'French Polynesia'),
                    (u'French Southern Territories', u'French Southern Territories'),
                    (u'Gabon', u'Gabon'),
                    (u'Gambia, The', 'Gambia, The'),
                    (u'Georgia', u'Georgia'),
                    (u'Germany', u'Germany'),
                    (u'Ghana', u'Ghana'),
                    (u'Gibraltar', u'Gibraltar'),
                    (u'Greece', u'Greece'),
                    (u'Greenland', u'Greenland'),
                    (u'Grenada', u'Grenada'),
                    (u'Guadeloupe', u'Guadeloupe'),
                    (u'Guam', u'Guam'),
                    (u'Guatemala', u'Guatemala'),
                    (u'Guernsey', u'Guernsey'),
                    (u'Guinea', u'Guinea'),
                    (u'Guinea-Bissau', u'Guinea-Bissau'),
                    (u'Guyana', u'Guyana'),
                    (u'Haiti', u'Haiti'),
                    (u'Heard Island and the McDonald Islands', u'Heard Island and the McDonald Islands'),
                    (u'Holy See', u'Holy See'),
                    (u'Honduras', u'Honduras'),
                    (u'Hong Kong', u'Hong Kong'),
                    (u'Hungary', u'Hungary'),
                    (u'Iceland', u'Iceland'),
                    (u'India', u'India'),
                    (u'Indonesia', u'Indonesia'),
                    (u'Iraq', u'Iraq'),
                    (u'Ireland', u'Ireland'),
                    (u'Isle of Man', u'Isle of Man'),
                    (u'Israel', u'Israel'),
                    (u'Italy', u'Italy'),
                    (u'Jamaica', u'Jamaica'),
                    (u'Japan', u'Japan'),
                    (u'Jersey', u'Jersey'),
                    (u'Jordan', u'Jordan'),
                    (u'Kazakhstan', u'Kazakhstan'),
                    (u'Kenya', u'Kenya'),
                    (u'Kiribati', u'Kiribati'),
                    (u'Korea, Republic of', 'Korea, Republic of'),
                    (u'Kosovo', u'Kosovo'),
                    (u'Kuwait', u'Kuwait'),
                    (u'Kyrgyzstan', u'Kyrgyzstan'),
                    (u'Lao People\'s Democratic Republic', u'Lao People\'s Democratic Republic'),
                    (u'Latvia', u'Latvia'),
                    (u'Lebanon', u'Lebanon'),
                    (u'Lesotho', u'Lesotho'),
                    (u'Liberia', u'Liberia'),
                    (u'Libya', u'Libya'),
                    (u'Liechtenstein', u'Liechtenstein'),
                    (u'Lithuania', u'Lithuania'),
                    (u'Luxembourg', u'Luxembourg'),
                    (u'Macao', u'Macao'),
                    (u'Macedonia, The Former Yugoslav Republic of', 'Macedonia, The Former Yugoslav Republic of'),
                    (u'Madagascar', u'Madagascar'),
                    (u'Malawi', u'Malawi'),
                    (u'Malaysia', u'Malaysia'),
                    (u'Maldives', u'Maldives'),
                    (u'Mali', u'Mali'),
                    (u'Malta', u'Malta'),
                    (u'Marshall Islands', u'Marshall Islands'),
                    (u'Martinique', u'Martinique'),
                    (u'Mauritania', u'Mauritania'),
                    (u'Mauritius', u'Mauritius'),
                    (u'Mayotte', u'Mayotte'),
                    (u'Mexico', u'Mexico'),
                    (u'Micronesia, Federated States of', 'Micronesia, Federated States of'),
                    (u'Moldova, Republic of', 'Moldova, Republic of'),
                    (u'Monaco', u'Monaco'),
                    (u'Mongolia', u'Mongolia'),
                    (u'Montenegro', u'Montenegro'),
                    (u'Montserrat', u'Montserrat'),
                    (u'Morocco', u'Morocco'),
                    (u'Mozambique', u'Mozambique'),
                    (u'Myanmar', u'Myanmar'),
                    (u'Namibia', u'Namibia'),
                    (u'Nauru', u'Nauru'),
                    (u'Nepal', u'Nepal'),
                    (u'Netherlands', u'Netherlands'),
                    (u'Netherlands Antilles', u'Netherlands Antilles'),
                    (u'New Caledonia', u'New Caledonia'),
                    (u'New Zealand', u'New Zealand'),
                    (u'Nicaragua', u'Nicaragua'),
                    (u'Niger', u'Niger'),
                    (u'Nigeria', u'Nigeria'),
                    (u'Niue', u'Niue'),
                    (u'Norfolk Island', u'Norfolk Island'),
                    (u'Northern Mariana Islands', u'Northern Mariana Islands'),
                    (u'Norway', u'Norway'),
                    (u'Oman', u'Oman'),
                    (u'Pakistan', u'Pakistan'),
                    (u'Palau', u'Palau'),
                    (u'Palestinian Territories', u'Palestinian Territories'),
                    (u'Panama', u'Panama'),
                    (u'Papua New Guinea', u'Papua New Guinea'),
                    (u'Paraguay', u'Paraguay'),
                    (u'Peru', u'Peru'),
                    (u'Philippines', u'Philippines'),
                    (u'Pitcairn', u'Pitcairn'),
                    (u'Poland', u'Poland'),
                    (u'Portugal', u'Portugal'),
                    (u'Puerto Rico', u'Puerto Rico'),
                    (u'Qatar', u'Qatar'),
                    (u'Reunion', u'Reunion'),
                    (u'Romania', u'Romania'),
                    (u'Russian Federation', u'Russian Federation'),
                    (u'Rwanda', u'Rwanda'),
                    (u'Saint Barthelemy', u'Saint Barthelemy'),
                    (u'Saint Helena, uAscension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'),
                    (u'Saint Kitts and Nevis', u'Saint Kitts and Nevis'),
                    (u'Saint Lucia', u'Saint Lucia'),
                    (u'Saint Martin', u'Saint Martin'),
                    (u'Saint Pierre and Miquelon', u'Saint Pierre and Miquelon'),
                    (u'Saint Vincent and the Grenadines', u'Saint Vincent and the Grenadines'),
                    (u'Samoa', u'Samoa'),
                    (u'San Marino', u'San Marino'),
                    (u'Sao Tome and Principe', u'Sao Tome and Principe'),
                    (u'Saudi Arabia', u'Saudi Arabia'),
                    (u'Senegal', u'Senegal'),
                    (u'Serbia', u'Serbia'),
                    (u'Seychelles', u'Seychelles'),
                    (u'Sierra Leone', u'Sierra Leone'),
                    (u'Singapore', u'Singapore'),
                    (u'Sint Maarten', u'Sint Maarten'),
                    (u'Slovakia', u'Slovakia'),
                    (u'Slovenia', u'Slovenia'),
                    (u'Solomon Islands', u'Solomon Islands'),
                    (u'Somalia', u'Somalia'),
                    (u'South Africa', u'South Africa'),
                    (u'South Georgia and the South Sandwich Islands', u'South Georgia and the South Sandwich Islands'),
                    (u'Spain', u'Spain'),
                    (u'Sri Lanka', u'Sri Lanka'),
                    (u'Suriname', u'Suriname'),
                    (u'Svalbard and Jan Mayen', u'Svalbard and Jan Mayen'),
                    (u'Swaziland', u'Swaziland'),
                    (u'Sweden', u'Sweden'),
                    (u'Switzerland', u'Switzerland'),
                    (u'Taiwan', u'Taiwan'),
                    (u'Tajikistan', u'Tajikistan'),
                    (u'Tanzania, uUnited Republic of', 'Tanzania, United Republic of'),
                    (u'Thailand', u'Thailand'),
                    (u'Timor-leste', u'Timor-leste'),
                    (u'Togo', u'Togo'),
                    (u'Tokelau', u'Tokelau'),
                    (u'Tonga', u'Tonga'),
                    (u'Trinidad and Tobago', u'Trinidad and Tobago'),
                    (u'Tunisia', u'Tunisia'),
                    (u'Turkey', u'Turkey'),
                    (u'Turkmenistan', u'Turkmenistan'),
                    (u'Turks and Caicos Islands', u'Turks and Caicos Islands'),
                    (u'Tuvalu', u'Tuvalu'),
                    (u'Uganda', u'Uganda'),
                    (u'Ukraine', u'Ukraine'),
                    (u'United Arab Emirates', u'United Arab Emirates'),
                    (u'United Kingdom', u'United Kingdom'),
                    (u'United States', u'United States'),
                    (u'United States Minor Outlying Islands', u'United States Minor Outlying Islands'),
                    (u'Uruguay', u'Uruguay'),
                    (u'Uzbekistan', u'Uzbekistan'),
                    (u'Vanuatu', u'Vanuatu'),
                    (u'Venezuela', u'Venezuela'),
                    (u'Vietnam', u'Vietnam'),
                    (u'Virgin Islands, British', 'Virgin Islands, British'),
                    (u'Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
                    (u'Wallis and Futuna', u'Wallis and Futuna'),
                    (u'Western Sahara', u'Western Sahara'),
                    (u'Yemen', u'Yemen'),
                    (u'Zambia', u'Zambia'),
                    (u'Zimbabwe', u'Zimbabwe')],
            render_kw={'placeholder': 'Address *'},
            default='United States')

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
                ('no', 'No')])
    provides_video_content = RadioField(
            'Do you provide video content for social media platforms? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')])
    trains_professional_athletes  = RadioField(
            'Do you train professional athletes? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')])
    sells_merchandise = RadioField(
            'Do you currently sell merchandise on your website? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')])
    has_blog = RadioField(
            'Do you have a blog or newsletter database? *',
            [
                InputRequired('Please select an answer.')
            ],
            choices=[
                ('yes', 'Yes'),
                ('no', 'No')])
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
            'First name',
            [
                InputRequired('Please enter your first name.')
            ],
            render_kw={'placeholder': 'First Name *'})
    last_name = TextField(
            'Last name',
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
            'Phone number',
            [
                InputRequired('Please enter your email address.'),
            ],
            render_kw={'placeholder': 'Phone Number *'})
    order_number = TextField(
            'Order number',
            [
                InputRequired('Please enter your order number.')
            ],
            render_kw={'placeholder': 'Order Number *'})
    address = FormField(AddressForm)
    is_damaged = BooleanField('Damaged')
    is_wrong_size = BooleanField('Wrong size')
    is_wrong_quantity = BooleanField('Received multiple')
    is_no_exchange = BooleanField('Return without exchange')
    exchange_information = TextField(
            'Exchange information',
            render_kw={'placeholder': 'Please enter the size and type of the glove you would like for your exchange, if applicable.'})
    product_image = FileField(
            'Product Image (If Damaged):',
            render_kw={'multiple': True})
    additional_notes = TextAreaField(
            'Additional notes',
            render_kw={'placeholder': 'Additional Notes'})
    submit = SubmitField('Submit')

class DrillForm(Form):
    name = TextField(
            'Full Name',
            [
                InputRequired('Please enter your full name.')
            ],
            render_kw={'placeholder': 'Full Name'})
    email = TextField(
            'Email',
            [
                InputRequired('Please enter your email address.'),
                Email('Please enter a valid email address.')
            ],
            render_kw={'placeholder': 'Email Address'})
    zip_code = TextField(
            'Zip Code',
            [
                InputRequired('Please enter your zip code.'),
            ],
            render_kw={'placeholder': 'Zip Code'})
    submit = SubmitField('Subscribe')

