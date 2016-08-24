from app import db
from sqlalchemy.dialects.postgresql import JSON


class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    miles = db.Column(db.Integer)
    json_data = db.Column(JSON)

    def __init__(self, miles, json_data ):
        self.url = url
        self.miles = miles
        self.json_data = json_data

    def __repr__(self):
        return '<id {}>'.format(self.id)
