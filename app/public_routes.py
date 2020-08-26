from flask import render_template

from app import app

@app.route("/", methods=["GET"])
def index():
  return render_template("public/index.html")

@app.route("/about", methods=["GET"])
def about():
  return render_template("public/about.html")

@app.route("/jinja", methods=["GET"])
def jinja():
  my_name = "Pedro Frohmut"
  age = 30
  languages = ["JavaScript", "CSharp", "Python"]
  friends = {
    "Tom": 30,
    "Amy": 60,
    "tony": 56,
    "Clarissa": 23
  }
  colors = ("Red", "Green", "Blue")
  cool = True
  def repeat(var):
      return var + " " + var
  return render_template(
    "public/jinja.html", 
    name = my_name, 
    age = age,
    languages = languages,
    friends = friends,
    colors = colors,
    cool = cool,
    repeat = repeat
  )
