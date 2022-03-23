import os
from flask import Flask
from lib.routes import routes

def create_app(db):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://voyage:voyage@{host}/voyage'.format(host=os.environ.get('DB_HOST'))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = 'supersecret'

    db.init_app(app)

    app.register_blueprint(routes)
    return app
