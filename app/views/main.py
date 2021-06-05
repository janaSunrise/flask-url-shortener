from flask import Blueprint, render_template, request

from app import limiter
from ..config import APP_NAME, GITHUB_URL

main = Blueprint("main", __name__, template_folder="templates")

APP_CONF = {"github_url": GITHUB_URL, "app_name": APP_NAME}


@main.route("/")
@limiter.exempt
def index():
    return render_template("index.html", base_api_url=request.host_url + "api", **APP_CONF)


@main.route("/info")
@limiter.exempt
def info():
    return render_template("info.html", base_api_url=request.host_url + "api", **APP_CONF)
