from flask import Flask, render_template, redirect, request, send_from_directory

app = Flask(__name__, instance_relative_config=True, static_folder='static')
app.url_map.strict_slashes = False
app.config.from_object('config')
app.config.from_pyfile('config.py')

if app.config['ENVIRONMENT'] == 'development':
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
def blog(path):
    return redirect('https://blog.powerhandz.com/' + path, 301)

@app.route('/boxing-mma')
def boxing_mma():
    return render_template('boxing-mma.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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

@app.route('/ourtime')
def ourtime():
    return render_template('ourtime.html')

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

@app.route('/ourtime')
def our_time():
    return render_template('ourtime.html')

if __name__ == '__main__':
    app.run()
