#!/usr/bin/python
from flask import Flask, render_template, request
import api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results",methods=["GET","POST"])
def results():
    if request.method == "GET":
        ingredients=request.args.get("search")
        ingredients=ingredients.split(",")
        results=api.getResults(ingredients)
        return render_template("results.html",ingredients=ingredients,results=results)

@app.route("/recipe/<id>")
def recipe(id):
    recipe=api.getRecipe(id)
    #Get the largest flavor and use it as tag to search for mix: recipe["flavors"]
    #print recipe
    return render_template("recipe.html",recipe=recipe)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
    app.run()
