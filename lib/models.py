from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Island(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(), nullable=False)

    def __init__(self, name, slug, description, location):
        self.name = name
        self.slug = slug
        self.description = description
        self.location = location
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    island_id = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
    offer = db.Column(db.Integer, nullable=False)

    def __init__(self, island_id, offer):
        self.island_id = island_id
        self.offer = offer