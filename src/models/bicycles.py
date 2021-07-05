from . import db

class Bicycle(db.Model):
    __tablename__ = "bicycle"

    id = db.Column(db.BigInteger(), primary_key=True)
    year = db.Column(db.Integer())
    make = db.Column(db.Unicode())
    model = db.Column(db.Unicode())


