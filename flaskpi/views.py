from flask import Blueprint, render_template, request

app = Blueprint('website', __name__, template_folder='templates')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/tutorials")
def tutorials():
    return render_template('tutorials/tutorials.html')


@app.route("/tutorials/<name>")
def tutorial(name):
    return render_template('tutorials/%s.html' % name)
