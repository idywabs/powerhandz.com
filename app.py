from flask import Flask, render_template, redirect, request, send_from_directory, flash
from forms import AffiliateApplication, ContactForm
from flask_mail import Message, Mail
from pprint import pprint

app = Flask(__name__, instance_relative_config=True, static_folder='static')
app.url_map.strict_slashes = False
app.config.from_object('config')
app.config.from_pyfile('config.py')

mail = Mail()
mail.init_app(app)

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
    if request.method == 'POST':
        if form.validate():
            msg = Message(
                    'POWERHANDZ Affiliate Application',
                    sender=form.email.data,
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
    elif request.method == 'GET':
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
    if request.method == 'POST':
        if form.validate():
            msg = Message(
                    'POWERHANDZ Contact Form',
                    sender=form.email.data,
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
    else:
        return render_template('contact.html', form=form)

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

@app.route('/future')
def future():
    return render_template('future.html')

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

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/return-policy')
def return_policy():
    return render_template('return-policy.html');

@app.route('/softball')
def softball():
    return render_template('softball.html')

@app.route('/team')
def team():
    return render_template('team.html')

# Redirects

@app.route('/affiliates-form')
def redirect_affiliates_form():
    return redirect(app.config['SITE_URL'] + '/affiliate-application', 301)

@app.route('/blog', defaults={'path': ''})
@app.route('/blog/<path:path>')
def redirect_blog(path):
    return redirect('https://blog.powerhandz.com/' + path, 301)

@app.route('/lifestyle')
def lifestyle():
    return redirect(app.config['SITE_URL'] + '/fitness', 301)

@app.route('/ourtime')
def redirect_ourtime():
    return redirect(app.config['SITE_URL'] + '/our-time', 301)

@app.route('/powertogive')
def redirect_powertogive():
    return redirect(app.config['SITE_URL'] + '/power-to-give', 301)

@app.route('/shop')
def redirect_shop():
    return redirect('https://shop.powerhandz.com/', 301)

@app.route('/shop/product/return-shipping')
def redirect_return_shipping():
    return redirect('http://secure.powerhandz.com/product/return-shipping', 302)

@app.route('/shop/return-exchange-policy')
def redirect_return_policy():
    return redirect(app.config['SITE_URL'] + '/return-policy', 301)

@app.route('/shop/returns')
def redirect_shop_returns():
    return redirect(app.config['SITE_URL'] + '/returns', 301)

@app.route('/returns')
def returns():
    return redirect('http://secure.powerhandz.com/returns', 302)

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
