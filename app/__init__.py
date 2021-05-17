from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

from .config import SQLALCHEMY_DB_URI, RATELIMIT_TIMING

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DB_URI

# Database
db = SQLAlchemy(app)

# Limiter
limiter = Limiter(app, key_func=get_remote_address, default_limits=[RATELIMIT_TIMING])
