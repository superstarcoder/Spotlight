from flask import Flask, render_template, flash, request, send_from_directory, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
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

#@app.route('/suggest')
#def suggest():
#    return render_template('suggest.html')

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



class ReusableForm(Form):
    @app.route("/suggest", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            searchQuery=request.form['search']

            print("---------------------------------")
            print(searchQuery)
            print("---------------------------------")
            return redirect(url_for('hello2'))

        return render_template('suggest.html', form=form)

    @app.route("/suggestForm", methods=['GET', 'POST'])
    def hello2():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':

            print("---------------------------------")
            print(request.form["song"])
            print("---------------------------------")
            return redirect(url_for('hello3'))


        return render_template('suggestForm.html', form=form)

    @app.route("/suggestForm2", methods=['GET', 'POST'])
    def hello3():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':

            print("---------------------------------")
            print(request.form["genre"])
            print("---------------------------------")
            return redirect(url_for('thankYou'))

        return render_template('suggestForm2.html', form=form)


if __name__ == "__main__":
    app.run()