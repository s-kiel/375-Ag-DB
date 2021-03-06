#app/init.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see
license.txt file for more information.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the Instance Config
app.config.from_object(os.environ['APP_SETTINGS'])


# Set up the database connection
from app.database import init_db
init_db()

# Load the routing table
from app import views
