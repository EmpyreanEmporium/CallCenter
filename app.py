# Setup
import os
import sqlite3
import csv

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import usd

#configure app
app = Flask(__name__)

# Custom USD filters
app.jinja_env.filters["usd"] = usd

# Session setup
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3("sqlite:///sqlite3/callcenter.db")



