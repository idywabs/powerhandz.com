from flask import Flask, render_template, redirect, request, send_from_directory
from forms import ContactForm

app = Flask(__name__, instance_relative_config=True, static_folder='static')
app.url_map.strict_slashes = False
app.config.from_object('config')
app.config.from_pyfile('config.py')

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/affiliates')
def affiliates():
    return render_template('affiliates.html')

@app.route('/affiliates-form')
def form_affiliates():
    return render_template('affiliates-form.html')

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')

@app.route('/basketball')
def basketball():
    return render_template('basketball.html')

@app.route('/blog', defaults={'path': ''})
@app.route('/blog/<path:path>')
def redirect_blog(path):
    return redirect('https://blog.powerhandz.com/' + path, 301)

@app.route('/boxing-mma')
def boxing_mma():
    return render_template('boxing-mma.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm
    if request.method == 'POST':
      if form.validate() == False:
        flash('All fields are required.')
        return render_template('contact.html', form=form)
      else:
        return 'Form posted.'
    elif request.method == 'GET':
    	return render_template('contact.html', form=form)

@app.route('/events')
def events():
    return render_template('events.html')

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

@app.route('/lifestyle')
def lifestyle():
    return redirect('/fitness', 301)

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/ourtime', defaults={'path': ''})
def redirect_ourtime(path):
    return redirect('/our-time' + path, 301)

@app.route('/our-time')
def our_time():
    return render_template('our-time.html')

@app.route('/powertogive', defaults={'path': ''})
def redirect_powertogive(path):
    return redirect('/power-to-give' + path, 301)

@app.route('/power-to-give')
def power_to_give():
    return render_template('power-to-give.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_files():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/softball')
def softball():
    return render_template('softball.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
