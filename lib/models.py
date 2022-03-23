from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Island(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(), nullable=False)
    offers = db.relationship('Offer', backref='island', lazy=True)

    def __init__(self, name, slug, description, location):
        self.name = name
        self.slug = slug
        self.description = description
        self.location = location

    @classmethod
    def island_with_offers(cls, slug):
        return Island.query.filter_by(slug=slug).join(Offer).first()
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    offer = db.Column(db.Integer, nullable=False)
    island_id = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)

    def __init__(self, name, offer):
        self.name = name
        self.offer = offer
