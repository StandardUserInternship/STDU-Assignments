from app import app
from flask import render_template

@app.route("/")
@app.route("/diceware")
def diceware():
    return render_template("diceware.html")