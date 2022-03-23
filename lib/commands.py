from flask import Blueprint
from lib.models import Island, db

commands = Blueprint('commands', __name__, template_folder='templates')

@commands.cli.command('rollback')
def rollback():
    db.drop_all()

@commands.cli.command('migrate')
def migrate():
    db.create_all()

@commands.cli.command('seed')
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
