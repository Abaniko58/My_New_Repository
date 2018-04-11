#from app import app
from flask import Flask, flash, redirect, render_template, request, session, Blueprint

################
#### config ####
################

start_blueprint = Blueprint('start', __name__)


@start_blueprint.route('/')
def index():
    guest = "Guest" + ","
    return render_template("/index2.html", Guest = guest)

@start_blueprint.route("/index/")
def index2():
    guest = "Guest" + ","
    return render_template("/index.html", Guest = guest)

@start_blueprint.route("/about/")
def about():
    guest = "Guest" + ","
    return render_template("/about.html", Guest=guest)

@start_blueprint.route("/news/")
def news():
#    guest = "Guest" + ","
    return render_template("/news.html")

@start_blueprint.route("/cont/")
def cont():
#    guest = "Guest" + ","
    return render_template("/cont.html")

@start_blueprint.route("/pages/")
def pages():
#    guest = "Guest" + ","
    return render_template("/pages.html")