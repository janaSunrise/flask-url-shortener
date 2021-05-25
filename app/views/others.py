from flask import Blueprint, redirect

from app import db, limiter
from ..models.shortened_link import ShortenedLink

others = Blueprint("others", __name__, template_folder="templates")


@others.route("/<short_url>")
@limiter.exempt
def redirect_to_url(short_url):
    link = ShortenedLink.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.redirect_url)
