from flask import Flask, render_template, flash, request, send_from_directory, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import SpotipyBackend.setup as setup
import SpotipyBackend.methods as methods
import SpotipyBackend.vars as vars
import backend
sp = setup.run()
username, userid = methods.userInfo(sp)
print(username, userid)


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
#hmmmm lets see if the disc thing works


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

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
            vars.suggestForm[userid] = {}
            vars.suggestForm[userid]["searchResults"] = methods.songs(sp, searchQuery)
            backend.editSuggestForm1(userid, vars)

            print("---------------------------------")
            print(searchQuery)
            print(vars.suggestForm)
            print("---------------------------------")

            return redirect(url_for('hello2'))

        return render_template('suggest.html', form=form)

    @app.route("/suggestForm", methods=['GET', 'POST'])
    def hello2():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            vars.suggestForm[userid]["chosenSong"] = request.form["song"].split(" - ")[0]

            backend.editSuggestForm2(userid, vars)

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
            chosenSong = vars.suggestForm[userid]["chosenSong"]
            for x in vars.suggestForm[userid]["searchResults"]:
                if x["name"].startswith(chosenSong):
                    vars.suggestForm[userid]["chosenSongData"] = x
                    vars.suggestForm[userid]["chosenSongData"]["genre"] = request.form["genre"]
                    print(vars.suggestForm)
                    # code for adding chosenSongData to main songs database
                    # code for calling backend to edit html file


            print("---------------------------------")
            print(request.form["genre"])
            print("---------------------------------")
            return redirect(url_for('thankYou'))

        return render_template('suggestForm2.html', form=form)


if __name__ == "__main__":
    app.run()