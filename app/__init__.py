from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import SQLALCHEMY_DB_URI, HOST, PORT, DEBUG

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DB_URI

# Database
db = SQLAlchemy(app)
