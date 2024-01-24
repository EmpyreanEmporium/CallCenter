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

db = SQL("sqlite:///sqlite3/callcenter.db")

# Cache 
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Log out by clearing session
    session.clear()

    # Return to index
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    #clear any possible other sessions
    session.clear()

    # Variable for avalability check for username
    exist = db.execute("SELECT * FROM employees WHERE username = ?", request.form.get("username"))

    if request.method == "GET":
        return render_template
    
    if request.method == "POST":
        # Check for empty field
        if not request.form.get("username"):
            return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    # Clear any user_ids
    session.clear()

    # Check forms for content
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html")
        
        elif not request.form.get("password"):
            return render_template("login.html")
        
        # Query database for username
        rows = db.execute("SELECT * FROM employees WHERE username = ?", request.form.get("username"))

        # Make sure username exist and passward is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html")
        
        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        #redirect for sucessful login
        return render_template("app.html")
         


