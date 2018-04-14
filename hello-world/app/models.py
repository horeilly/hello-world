from app import db
from datetime import datetime as dt
import json


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)


class Bond(db.Model):

    __tablename__ = "bonds"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    company = db.Column(db.String(4))
    overnight = db.Column(db.Float)
    _7_day = db.Column(db.Float)
    _15_day = db.Column(db.Float)
    _30_day = db.Column(db.Float)
    _60_day = db.Column(db.Float)
    _90_day = db.Column(db.Float)

    def __repr__(self):
        data = {
          "date": dt.strftime(self.date, "%Y-%m-%d"),
          "company": self.company,
          "overnight": self.overnight,
          "_7_day": self._7_day,
          "_15_day": self._15_day,
          "_30_day": self._30_day,
          "_60_day": self._60_day,
          "_90_day": self._90_day
        }
        return json.dumps(data, indent=2)
