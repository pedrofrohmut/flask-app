from flask import render_template

from app import app

@app.route("/", methods=["GET"])
def index():
    return render_template("public/index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("public/about.html")

