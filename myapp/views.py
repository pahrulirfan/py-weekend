from flask import render_template, redirect, url_for
from .create_app import app
from .models import Profile

@app.route("/")
def index():
    return render_template("index.html",title="Home")


# setting routing ke about
@app.route("/about/<nickname>")
def about(nickname=None):
    projects = [
        "Website Kota Mataram",
        "Website RS",
        "Website Gubernur"
    ]

    profile = Profile.query.filter(
        Profile.nickname == nickname
    ).first()

    # profile = {
    #     "name": "Pahrul Irfan",
    #     "address": "Mataram"
    # }
    return render_template("about.html", title="About", projects=projects, profile=profile)

@app.route("/new_profile")
def new_profile():
    profile = Profile()
    profile.firstname = "Pahrul 2"
    profile.lastname = 'Irfan 2'
    profile.nickname = 'Ganteng 2'
    profile.address = 'Mataram 2'
    profile.work = 'Nganggur 2'
    profile.email = "Nganggur@gmail.com 2"

    profile.save()
    return redirect(url_for('about', nickname=profile.nickname))