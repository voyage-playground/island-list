from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://voyage:voyage@database/voyage'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecret'

db = SQLAlchemy(app)

class Island(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(), nullable=False)

    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

@app.route("/")
def home():
    islands = Island.query.all()
    return render_template('home.j2', islands=islands)
