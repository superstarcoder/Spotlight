from flask import Flask, render_template, flash, request, send_from_directory, redirect, url_for
import os


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
#hmmmm lets see if the disc thing works


if __name__ == "__main__":
    app.run()