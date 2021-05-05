from flask import Blueprint, Response, jsonify, redirect, request, render_template

from app import db
from .config import GITHUB_URL
from .models import ShortenedLink

views = Blueprint("/views", __name__, template_folder="templates")


@views.route("/")
def index():
    return render_template("index.html", base_url=request.host_url, github_url=GITHUB_URL)


@views.route("/info")
def info():
    return render_template("info.html", base_url=request.host_url, github_url=GITHUB_URL)


@views.route("/<short_url>")
def redirect_to_url(short_url):
    link = ShortenedLink.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.redirect_url)


@views.route("/api/shorten")
def api_url_shorten():
    request_data = request.args

    if not request_data or "redirect_url" not in request_data:
        return Response("Please enter a redirect URL!", 400)

    url = request_data["redirect_url"]

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    shortened_link_obj = ShortenedLink(redirect_url=url)
    db.session.add(shortened_link_obj)
    db.session.commit()

    return jsonify({"shortened_url": request.host_url + shortened_link_obj.short_url}), 200


@views.route("/api/info")
def api_info():
    request_data = request.args

    if not request_data or "code" not in request_data:
        return Response("Please enter a Shortened URL code or the URL!", 400)

    code = request_data["code"]
    if code.startswith(request.host_url):
        code = code.replace(request.host_url, "")

    link = ShortenedLink.query.filter_by(short_url=code).first_or_404()
    return jsonify(
        {"visits": link.visits, "created": link.date_created, "redirects_to": link.redirect_url}
    ), 200
