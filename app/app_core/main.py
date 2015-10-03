from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("home.html")

@application.route("/aboutus")
def about_us():
    return render_template("aboutus.html")


@application.route("/contactus")
def contact_us():
    return render_template("contactus.html")

@application.route("/events")
def events():
    return render_template("events.html")

@application.route("/gallery")
def gallery():
    return render_template("gallery.html")

@application.route("/register")
def register():
    return render_template("registration.html")
