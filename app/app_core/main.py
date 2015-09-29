from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/test")
def show_test():
    return "<h1>I think charles is going to break things here?</h1>"
