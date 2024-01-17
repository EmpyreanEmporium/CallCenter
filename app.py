# Setup
import os
import sqlite3
import csv

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


from helpers import usd, login_required

#configure app
app = Flask(__name__)

# Custom USD filters
app.jinja_env.filters["usd"] = usd

# Session setup
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///callcenter.db")

@app.route("/login", methods=["GET", "POST"])
def login():

    #clear any user_ids
    session.clear()

    # POST
    if not request.form.get("username"):
        return render_template("login.html")


@app.route("/", method=["GET", "POST"])
@login_required
def index():
    return render_template("login.html")

