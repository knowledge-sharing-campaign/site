from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/test")
def show_test():
    return "<h1>This is a conflict on the test Route</h1>"

