from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def serve_home():
    return render_template("home.html")


@application.route("/test")
def show_test():
    return "<h1>I think charles is going to break things here?</h1>"
