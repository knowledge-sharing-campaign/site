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

@application.route("/register")
def register():
    parsed_content = minidom.parseString(requests.get('http://textcaptcha.com/api').content)
    question = parsed_content.getElementsByTagName('question')[0].childNodes[0].nodeValue
    answers = []
    
    for node in parsed_content.getElementsByTagName('answer')[0].childNodes:
        answers.append(node.nodeValue)

    return render_template("registration.html",
        question=question,
        answers=' '.join(answers)
    )