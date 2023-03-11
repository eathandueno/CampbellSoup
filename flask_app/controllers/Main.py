from flask_app import app
from flask import render_template, redirect, session,flash,request
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/services')
def services_page():
    return render_template("services.html")

@app.route('/beforeAfter')
def before_page():
    return render_template("beforeAfter.html")

@app.route('/covid')
def covid_page():
    return render_template("covid.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")