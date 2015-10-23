import requests
from xml.dom import minidom
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

@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/register")
def register():
    return render_template("register.html")

@application.route("/privacy")
def privacy():
    return render_template("privacy.html")

@application.route("/partners")
def partners():
    return render_template("partners.html")

@application.route("/termscons")
def termscons():
    return render_template("termscons.html")

# @application.route("/forum")
# def forum():
#     return render_template("forum.html")