import random
import string
from datetime import datetime

from app import db
from .utils import b62_encode


class ShortenedLink(db.Model):
    __tablename__ = "shortened_link"

    id = db.Column(db.Integer, primary_key=True, unique=True)

    short_url = db.Column(db.String(), unique=True)
    redirect_url = db.Column(db.String())

    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def __repr__(self):
        return f"<{self.__class__.__name__} slug={self.slug} redirect_url={self.redirect_url}>"

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(random.choices(characters, k=random.randint(1, 8)))

        last_record_id = self.query.count()
        base62_encoded_id = b62_encode(last_record_id)
        short_url += base62_encoded_id

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        return short_url
