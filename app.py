from flask import Flask, render_template, redirect, request, send_from_directory, flash
from forms import AffiliateApplication, ContactForm, DrillForm, ReturnForm
from flask_mail import Attachment, Message, Mail
from datetime import datetime
from werkzeug.utils import secure_filename
import stripe

# Initialization

app = Flask(__name__, instance_relative_config=True, static_folder='static')
app.url_map.strict_slashes = False
app.config.from_object('config')
app.config.from_pyfile('config.py')

mail = Mail()
mail.init_app(app)

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Pages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/affiliates')
def affiliates():
    return render_template('affiliates.html')

@app.route('/affiliate-application', methods=['GET', 'POST'])
def affiliate_application():
    form = AffiliateApplication()
    if request.method == 'GET':
        return render_template('affiliate-application.html', form=form)
    else:
        if form.validate():
            msg = Message(
                    'POWERHANDZ Affiliate Application ' + str(datetime.utcnow()) + ' UTC',
                    sender=app.config['DEFAULT_SENDER_ADDRESS'],
                    recipients=[app.config['AFFILIATE_APPLICATION_RECIPIENT']])
            msg.body = 'This message was automatically generated from %s.\n\n'\
                    % (app.config['SITE_URL'] + request.path)
            for field in form:
                if field.type not in ['CSRFTokenField', 'SubmitField']:
                    msg.body += '%s: %s\n' % (field.label.text, field.data)
            mail.send(msg)
            return render_template('affiliate-application.html', form=form, success=True)
        else:
            flash('All fields are required.')
            return render_template('affiliate-application.html', form=form)

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')

@app.route('/basketball')
def basketball():
    return render_template('basketball.html')

@app.route('/boxing-mma')
def boxing_mma():
    return render_template('boxing-mma.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'GET':
        return render_template('contact.html', form=form)
    else:
        if form.validate():
            msg = Message(
                    'POWERHANDZ Contact Form ' + str(datetime.utcnow()) + ' UTC',
                    sender=app.config['DEFAULT_SENDER_ADDRESS'],
                    recipients=[app.config['CONTACT_FORM_RECIPIENT']])
            msg.body = 'This message was automatically generated from %s.\n\n'\
                    % (app.config['SITE_URL'] + request.path)
            for field in form:
                if field.type not in ['CSRFTokenField', 'SubmitField']:
                    msg.body += '%s: %s\n' % (field.label.text, field.data)
            mail.send(msg)
            return render_template('contact.html', form=form, success=True)
        else:
            flash('All fields are required.')
            return render_template('contact.html', form=form)

@app.route('/essence', methods=['GET', 'POST'])
def essence():
    form = DrillForm()
    if request.method == 'GET':
        return render_template('essence.html', form=form)
    else:
        if form.validate():
            msg = Message(
                    'POWERHANDZ Essence Form ' + str(datetime.utcnow()) + ' UTC',
                    sender=app.config['DEFAULT_SENDER_ADDRESS'],
                    recipients=[app.config['DRILL_FORM_RECIPIENT']])
            msg.body = 'This message was automatically generated from %s.\n\n'\
                    % (app.config['SITE_URL'] + request.path)
            for field in form:
                if field.type not in ['CSRFTokenField', 'SubmitField']:
                    msg.body += '%s: %s\n' % (field.label.text, field.data)
            mail.send(msg)
            return render_template('essence.html', form=form, success=True)
        else:
            flash('All fields are required.')
            return render_template('essence.html', form=form)

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

@app.route('/football')
def football():
    return render_template('football.html')

@app.route('/football-training', methods=['GET', 'POST'])
def football_training():
    form = DrillForm()
    if request.method == 'GET':
        return render_template('football-training.html', form=form)
    else:
        if form.validate():
            msg = Message(
                    'POWERHANDZ Drill Form ' + str(datetime.utcnow()) + ' UTC',
                    sender=app.config['DEFAULT_SENDER_ADDRESS'],
                    recipients=[app.config['DRILL_FORM_RECIPIENT']])
            msg.body = 'This message was automatically generated from %s.\n\n'\
                    % (app.config['SITE_URL'] + request.path)
            for field in form:
                if field.type not in ['CSRFTokenField', 'SubmitField']:
                    msg.body += '%s: %s\n' % (field.label.text, field.data)
            mail.send(msg)
            return render_template('football-training.html', form=form, success=True)
        else:
            flash('All fields are required.')
            return render_template('football-training.html', form=form)

@app.route('/handz-of-the-future')
def handz_of_the_future():
    return render_template('handz-of-the-future.html')

@app.route('/golf')
def golf():
    return render_template('golf.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/our-time')
def our_time():
    return render_template('our-time.html')

@app.route('/power-to-give')
def power_to_give():
    return render_template('power-to-give.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/press/releases/2018-nfl-draft')
def release_2018_nfl_draft():
    return render_template('releases/2018-nfl-draft-release.html')

@app.route('/press/resources')
def resources():
    return render_template('resources.html')

@app.route('/return-policy')
def return_policy():
    return render_template('return-policy.html');

@app.route('/returns', methods=['GET', 'POST'])
def returns():
    form = ReturnForm()
    if request.method == 'GET':
        return render_template('returns.html', form=form)
    else:
        if form.validate():
            msg = Message(
                    'POWERHANDZ Return Request ' + str(datetime.utcnow()) + ' UTC',
                    sender=app.config['DEFAULT_SENDER_ADDRESS'],
                    recipients=[app.config['RETURN_FORM_RECIPIENT']])
            msg.body = 'This message was automatically generated from %s.\n\n'\
                    % (app.config['SITE_URL'] + request.path)
            for field in form:
                if field.type not in [
                        'CSRFTokenField',
                        'FileField',
                        'FormField',
                        'SubmitField']:
                    msg.body += '%s: %s\n' % (field.label.text, field.data)
                elif field.type == 'FormField':
                    for subfield in field:
                        msg.body += '%s: %s\n' % (subfield.label.text, subfield.data)
                elif field.type == 'FileField':
                    for file_object in request.files.getlist(field.name):
                        msg.attach(
                                secure_filename(file_object.filename),
                                file_object.headers['Content-Type'],
                                file_object.read())
            mail.send(msg)
            return render_template('returns.html', form=form, success=True)
        else:
            flash('All fields are required.')
            return render_template('returns.html', form=form)

@app.route('/return-shipping', methods=['GET', 'POST'])
def return_shipping():
    form = ReturnForm(prefix="returns")
    if request.method == 'GET':
        return render_template('return-shipping.html', form=form)
    else:
        error = None

        if form.validate():
            amount = 1000
            notify = False

            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    description='POWERHANDZ Restocking Fee',
                    source=request.form['stripeToken']
                )

                msg = Message(
                        'POWERHANDZ Return Request ' + str(datetime.utcnow()) + ' UTC',
                        sender=app.config['DEFAULT_SENDER_ADDRESS'],
                        recipients=[app.config['RETURN_FORM_RECIPIENT']])
                msg.body = 'This message was automatically generated from %s.\n\n'\
                        % (app.config['SITE_URL'] + request.path)
                for field in form:
                    if field.type not in [
                            'CSRFTokenField',
                            'FileField',
                            'FormField',
                            'SubmitField']:
                        msg.body += '%s: %s\n' % (field.label.text, field.data)
                    elif field.type == 'FormField':
                        for subfield in field:
                            msg.body += '%s: %s\n' % (subfield.label.text, subfield.data)
                    elif field.type == 'FileField':
                        for file_object in request.files.getlist(field.name):
                            msg.attach(
                                    secure_filename(file_object.filename),
                                    file_object.headers['Content-Type'],
                                    file_object.read())
                msg.body += '\nSuccessful charge: %s' % charge.id
                mail.send(msg)

                return render_template('return-shipping.html', form=form, success=True)
            except stripe.error.CardError, e:
                error = e.json_body['error']['message']
                pass
            except stripe.error.RateLimitError, e:
                error = e.json_body['error']['message']
                pass
            except stripe.error.InvalidRequestError, e:
                error = e.json_body['error']['message']
                pass
            except stripe.error.AuthenticationError, e:
                error = e.json_body['error']['message']
                pass
            except stripe.error.APIConnectionError, e:
                error = e.json_body['error']['message']
                notify = True
                pass
            except stripe.error.StripeError, e:
                error = e.json_body['error']['message']
                notify = True
                pass
            except Exception, e:
                error = 'There was an unexpected error. Please try again later.'
                notify = True
                raise

            if notify:
                msg = Message(
                        'Error: POWERHANDZ Return Request',
                        sender=app.config['DEFAULT_SENDER_ADDRESS'],
                        recipients=[app.config['DEFAULT_ERROR_NOTIFICATION_ADDRESS']])
                msg.body = 'This message was automatically generated from %s.\n\n'\
                        % (app.config['SITE_URL'] + request.path)
                msg.body += 'Error Message: %s\n\n' % error
                for field in form:
                    if field.type not in [
                            'CSRFTokenField',
                            'FileField',
                            'FormField',
                            'SubmitField']:
                        msg.body += '%s: %s\n' % (field.label.text, field.data)
                    elif field.type == 'FormField':
                        for subfield in field:
                            msg.body += '%s: %s\n' % (subfield.label.text, subfield.data)
                    elif field.type == 'FileField':
                        for file_object in request.files.getlist(field.name):
                            msg.attach(
                                    secure_filename(file_object.filename),
                                    file_object.headers['Content-Type'],
                                    file_object.read())
                mail.send(msg)

        return render_template('return-shipping.html', form=form, success=False, error=error)

@app.route('/softball')
def softball():
    return render_template('softball.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/voices-of-greatness')
def voices_of_greatness():
    return render_template('voices-of-greatness.html')

# Redirects

@app.route('/affiliates-form')
def redirect_affiliates_form():
    return redirect(app.config['SITE_URL'] + '/affiliate-application', 301)

@app.route('/blog', defaults={'path': ''})
@app.route('/blog/<path:path>')
def redirect_blog(path):
    return redirect('https://blog.powerhandz.com/' + path, 301)

@app.route('/future')
def redirect_future():
    return redirect(app.config['SITE_URL'] + '/handz-of-the-future', 301)

@app.route('/lifestyle')
def lifestyle():
    return redirect(app.config['SITE_URL'] + '/fitness', 301)

@app.route('/ourtime')
def redirect_ourtime():
    return redirect(app.config['SITE_URL'] + '/our-time', 301)

@app.route('/powertogive')
def redirect_powertogive():
    return redirect(app.config['SITE_URL'] + '/power-to-give', 301)

@app.route('/resources')
def redirect_resources():
    return redirect(app.config['SITE_URL'] + '/press/resources', 301)

@app.route('/shop')
def redirect_shop():
    return redirect('https://shop.powerhandz.com/', 301)

@app.route('/shop/product/return-shipping')
def redirect_return_shipping():
    return redirect(app.config['SITE_URL'] + '/return-shipping', 301)

@app.route('/shop/return-exchange-policy')
def redirect_return_policy():
    return redirect(app.config['SITE_URL'] + '/return-policy', 301)

@app.route('/shop/returns')
def redirect_shop_returns():
    return redirect(app.config['SITE_URL'] + '/returns', 301)

@app.route('/voices')
def redirect_voices():
    return redirect(app.config['SITE_URL'] + '/voices-of-greatness', 301)

# Static Files

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_files():
    return send_from_directory(app.static_folder, request.path[1:])

if app.config['ENVIRONMENT'] == 'production' or \
   app.config['ENVIRONMENT'] == 'staging':
    @app.route('/css/<path:path>')
    def redirect_css(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/css/' + path, 301)
    @app.route('/files/<path:path>')
    def redirect_files(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/files/' + path, 301)
    @app.route('/fonts/<path:path>')
    def redirect_fonts(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/fonts/' + path, 301)
    @app.route('/images/<path:path>')
    def redirect_images(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/images/' + path, 301)
    @app.route('/img/<path:path>')
    def redirect_img(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/images/' + path, 301)
    @app.route('/js/<path:path>')
    def redirect_js(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/js/' + path, 301)
    @app.route('/vid/<path:path>')
    def redirect_vid(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/videos/' + path, 301)
    @app.route('/videos/<path:path>')
    def redirect_videos(path):
        return redirect(app.config['ASSET_BASE_URL'] + '/videos/' + path, 301)

elif app.config['ENVIRONMENT'] == 'development':
    @app.route('/css/<path:path>')
    def css(path):
        return send_from_directory('assets/css', path)
    @app.route('/files/<path:path>')
    def files(path):
        return send_from_directory('assets/files', path)
    @app.route('/fonts/<path:path>')
    def fonts(path):
        return send_from_directory('assets/fonts', path)
    @app.route('/images/<path:path>')
    def images(path):
        return send_from_directory('assets/images', path)
    @app.route('/js/<path:path>')
    def js(path):
        return send_from_directory('assets/js', path)
    @app.route('/videos/<path:path>')
    def videos(path):
        return send_from_directory('assets/videos', path)

# Error Pages

@app.errorhandler(403)
def page_not_found(e):
    return render_template(
            'error.html',
            error_code='403',
            error_message='Page Forbidden',
            error_details='You do not have permission to access this URL.'
            ), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
            'error.html',
            error_code='404',
            error_message='Page Not Found',
            error_details='The requested URL was not found on this server.'
            ), 404

@app.errorhandler(410)
def page_not_found(e):
    return render_template(
            'error.html',
            error_code='410',
            error_message='Link No Longer Available',
            error_details='We\'re sorry. The link you clicked on is no longer available'
            ), 410

@app.errorhandler(500)
def page_not_found(e):
    return render_template(
            'error.html',
            error_code='500',
            error_message='Internal Server Error',
            error_details='There was an error. Please try again later.'
            ), 500

if __name__ == '__main__':
    app.run()
