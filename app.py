import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://voyage:voyage@{host}/voyage'.format(host=os.environ.get('DB_HOST'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecret'

db = SQLAlchemy(app)

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

@app.route("/")
def home():
    islands = Island.query.all()
    return render_template('home.j2', islands=islands)

@app.route("/islands/<string:slug>", methods=['GET'])
def get_island(slug):
    island = Island.query.filter_by(slug=slug).first()
    return render_template('island.j2', island=island)

@app.route("/islands/<string:slug>", methods=['POST'])
def add_offer(slug):
    island = Island.query.filter_by(slug=slug).first()
    offer = Offer(island_id=island.id,offer=request.form['offer'])
    db.session.add(offer)
    db.session.commit()
    return render_template('island.j2', island=island)

@app.cli.command('rollback')
def rollback():
    db.drop_all()

@app.cli.command('migrate')
def migrate():
    db.create_all()

@app.cli.command('seed')
def seed():
   island1 = Island(name="Super Private Island",
                        slug="super-private-island",
                        description="Once owned by a king, this beauty can now be yours.",
                        location="50.474534, -34.297446")
   island2 = Island(name="Platform in the Middle of International Waters",
                        slug="platform-in-the-middle",
                        description="Modeled after the famous Rose Island but better.",
                        location="58.273698, 1.983231")
   island3 = Island(name="Luxury Island with Bunker",
                        slug="luxury-island-bunker",
                        description="Survive the end of the world in style in this beautiful island.",
                        location="13.501421, -135.080818")
   island4 = Island(name="Smallest Island Ever",
                        slug="smallest-island",
                        description="Want to own an island without breaking the bank? This is for you.",
                        location="60.233861, -91.731105")
   island5 = Island(name="Frozen Island with igloo",
                        slug="frozen-island-with-igloo",
                        description="The current owner has already built several tiny igloos awaiting your arrival.",
                        location="78.120248, -136.333475")
   island6 = Island(name="Jurassic Island",
                        slug="jurassic-island",
                        description="Legend has it this island is populated with mysterious mythical creatures.",
                        location="-2.258883, 65.378591")
   db.session.add(island1)
   db.session.add(island2)
   db.session.add(island3)
   db.session.add(island4)
   db.session.add(island5)
   db.session.add(island6)
   db.session.commit()