HOST = "127.0.0.1"
PORT = 5000
DEBUG = True

# -- APP Config --
APP_NAME = "Flask URL Shortener"
GITHUB_URL = "https://github.com/janaSunrise/flask-url-shortener"

# -- Database --
SQLALCHEMY_DB_URI = f"sqlite:///app.db"

# -- Ratelimiting --
# Use this following format for ratelimits: `<Number of requests> per <Amount of time> <Unit of time>`
# Example: `2 per 1 second` or `1 per 2 seconds`
RATELIMIT_TIMING = "1 per 1 second"
