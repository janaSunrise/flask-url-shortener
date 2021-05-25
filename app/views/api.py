from flask import Blueprint, Response, jsonify, request

from app import db, limiter
from ..models.shortened_link import ShortenedLink

api = Blueprint("api", __name__, template_folder="templates", url_prefix="/api")


@api.route("/shorten")
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

    return (
        jsonify({"shortened_url": request.host_url + shortened_link_obj.short_url}),
        200,
    )


@api.route("/info")
@limiter.exempt
def api_url_info():
    request_data = request.args

    if not request_data or "code" not in request_data:
        return Response("Please enter a Shortened URL code or the URL!", 400)

    code = request_data["code"]
    if code.startswith(request.host_url):
        code = code.replace(request.host_url, "")

    link = ShortenedLink.query.filter_by(short_url=code).first_or_404()
    return (
        jsonify(
            {
                "visits": link.visits,
                "created": link.date_created,
                "redirects_to": link.redirect_url,
            }
        ),
        200,
    )
