from flask import Blueprint, render_template, request

app = Blueprint('website', __name__, template_folder='templates')


@app.route("/")
def index_view():
    return render_template('index.html')
