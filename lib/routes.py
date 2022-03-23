import logging
from flask import Blueprint, redirect, render_template, url_for
from lib.models import Island, Offer, db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class AddOfferForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    offer = IntegerField('offer', validators=[DataRequired()])

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route("/")
def home():
    islands = Island.query.all()
    return render_template('home.j2', islands=islands)

@routes.route("/<string:slug>", methods=['GET'])
def get_island(slug):
    form = AddOfferForm()
    island = Island.island_with_offers(slug)
    return render_template('island.j2', island=island, form=form)

@routes.route("/<string:slug>", methods=['POST'])
def add_offer(slug):
    form = AddOfferForm()
    if form.validate_on_submit():
        name = form.name.data
        offer = form.offer.data
        island = Island.query.filter_by(slug=slug).first()
        offer = Offer(name=name,offer=offer)
        island.offers.append(offer)
        db.session.add(island)
        db.session.commit()
        return redirect(url_for('routes.get_island', slug=island.slug))
    return redirect(url_for('routes.home'))
