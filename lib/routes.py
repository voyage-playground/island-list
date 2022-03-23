from flask import Blueprint, render_template, request
from lib.models import Island, Offer, db

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route("/")
def home():
    islands = Island.query.all()
    return render_template('home.j2', islands=islands)

@routes.route("/islands/<string:slug>", methods=['GET'])
def get_island(slug):
    island = Island.query.filter_by(slug=slug).first()
    return render_template('island.j2', island=island)

@routes.route("/islands/<string:slug>", methods=['POST'])
def add_offer(slug):
    island = Island.query.filter_by(slug=slug).first()
    offer = Offer(island_id=island.id,offer=request.form['offer'])
    db.session.add(offer)
    db.session.commit()
    return render_template('island.j2', island=island)