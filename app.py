#!/usr/bin/python
from flask import Flask, render_template, request
#import api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/recipe/<id>")
def recipe():
    return render_template("recipe.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
    app.run()
