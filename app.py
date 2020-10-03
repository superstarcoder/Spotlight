from flask import Flask, render_template, flash, request, send_from_directory, redirect, url_for
import os


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
#hmmmm lets see if the disc thing works


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/fonts/<path:path>')
def fonts(path):
    return send_from_directory('templates/fonts',path)

@app.route('/img/<path:path>')
def img(path):
    return send_from_directory('templates/img',path)

@app.route('/sass/<path:path>')
def sass(path):
    return send_from_directory('templates/sass',path)

@app.route('/Source/<path:path>')
def Source(path):
    return send_from_directory('templates/Source',path)

@app.route('/css/<path:path>')
def css(path):
    return send_from_directory('templates/css',path)

@app.route('/js/<path:path>')
def js(path):
    return send_from_directory('templates/js',path)


if __name__ == "__main__":
    app.run()