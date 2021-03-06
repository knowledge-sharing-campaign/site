import __builtin__
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ksc.db'
__builtin__.ksc_db = SQLAlchemy(application)

from manage_user import *


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


@application.route("/login")
def login():
    return render_template("login.html")


@application.route("/register")
def register():
    return render_template("register.html")


@application.route("/adduser", methods=['POST'])
def add():
    add_user(request)

    return "<h1>Registered successfully</h1>"


@application.route("/privacy")
def privacy():
    return render_template("privacy.html")


@application.route("/partners")
def partners():
    return render_template("partners.html")


@application.route("/termscons")
def termscons():
    return render_template("termscons.html")


@application.route("/reset")
def reset():
    return render_template("forgotpassword.html")


@application.route("/charles")
def charles():
    return render_template("charles.html")


@application.route("/rahul")
def rahul():
<<<<<<< HEAD
    return render_template("rahul.html")     

@application.route("/forum")
def forum():
    return render_template("forum.html")

@application.route("/registrationsuccessful")
def registrationsuccessful():
    return render_template("registrationsuccessful.html")
=======
    return render_template("rahul.html")
>>>>>>> f3e908c195ee299e739b1a589557a25e621c4f4e
