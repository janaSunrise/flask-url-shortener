from flask import Blueprint, Response, jsonify, redirect, request

from app import db
from .models import ShortenedLink

views = Blueprint("/views", __name__, template_folder="templates")

@views.route('/<short_url>')
def redirect_to_url(short_url):
    link = ShortenedLink.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.redirect_url)


@views.route("/api/shorten")
def api_url_shorten():
    request_data = request.args

    if not request_data or "redirect_url" not in request_data:
        return Response("Please enter a valid POST request!", 400)

    url = request_data["redirect_url"]
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    shortened_link_obj = ShortenedLink(redirect_url=url)
    db.session.add(shortened_link_obj)
    db.session.commit()

    return jsonify({"short_url": request.host_url + shortened_link_obj.short_url}), 200
