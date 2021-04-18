from flask import Blueprint, redirect

from app import db
from .models import ShortenedLink

views = Blueprint("/views", __name__, template_folder="templates")

@views.route('/<short_url>')
def redirect_to_url(short_url):
    link = ShortenedLink.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.redirect_url)
