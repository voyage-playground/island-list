from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    islands = ['island1', 'island2', 'island3']
    return render_template('home.j2', islands=islands)