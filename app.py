from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

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

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')

@app.route('/basketball')
def basketball():
    return render_template('basketball.html')

@app.route('/boxing-mma')
def boxing_mma():
    return render_template('boxing-mma.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/events')
def events():
    return render_template('events.html')

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
    return render_template('lifestyle.html')

@app.route('/ourtime')
def ourtime():
    return render_template('ourtime.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')
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
