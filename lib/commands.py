from flask import Blueprint
from lib.models import Island, Offer, db

def rollback():
    db.drop_all()

def migrate():
    db.create_all()

def seed():
    island1 = Island(name="Super Private Island",
                        slug="super-private-island",
                        description="Once owned by a king, this beauty can now be yours.",
                        location="50.474534, -34.297446")
    offer1 = Offer(name="Jaden",offer=20)
    island1.offers.append(offer1)

    island2 = Island(name="Platform in the Middle of International Waters",
                        slug="platform-in-the-middle",
                        description="Modeled after the famous Rose Island but better.",
                        location="58.273698, 1.983231")
    offer = Offer(name="Dan",offer=40)
    island2.offers.append(offer)

    island3 = Island(name="Luxury Island with Bunker",
                        slug="luxury-island-bunker",
                        description="Survive the end of the world in style in this beautiful island.",
                        location="13.501421, -135.080818")
    offer = Offer(name="Rachel",offer=140)
    island3.offers.append(offer)

    island4 = Island(name="Smallest Island Ever",
                        slug="smallest-island",
                        description="Want to own an island without breaking the bank? This is for you.",
                        location="60.233861, -91.731105")
    offer = Offer(name="Roger",offer=2)
    island4.offers.append(offer)

    island5 = Island(name="Frozen Island with igloo",
                        slug="frozen-island-with-igloo",
                        description="The current owner has already built several tiny igloos awaiting your arrival.",
                        location="78.120248, -136.333475")
    offer = Offer(name="Justin",offer=22)
    island5.offers.append(offer)

    island6 = Island(name="Jurassic Island",
                        slug="jurassic-island",
                        description="Legend has it this island is populated with mysterious mythical creatures.",
                        location="-2.258883, 65.378591")
    offer = Offer(name="Tristin",offer=32)
    island6.offers.append(offer)

    db.session.add_all([island1, island2, island3, island4, island5, island6])
    db.session.commit()
