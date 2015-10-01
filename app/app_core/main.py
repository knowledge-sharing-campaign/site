from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def serve_home():
    return render_template("home.html")
