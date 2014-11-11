
#!/usr/bin/python
from flask import Flask, render_template, request
import api, operator, random 

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
    if "holiday" in recipe["attributes"].keys():
        tags= recipe["attributes"]["holiday"][random.randrange(0,len(recipe["attributes"]["holiday"]))]
    elif "cuisine" in recipe["attributes"].keys():
        tags= recipe["attributes"]["cuisine"][random.randrange(0,len(recipe["attributes"]["cuisine"]))]
    elif len(recipe["flavors"]) > 0:
        print recipe["flavors"]
        tags=  max(recipe["flavors"].iteritems(), key=operator.itemgetter(1))[0]
    else:
        tags=recipe["name"].split(" ")[0]
    #Get the largest flavor and use it as tag to search for mix: recipe["flavors"]
    #print recipe
    return render_template("recipe.html",recipe=recipe, url=api.getSong(tags), tag=tags)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
    app.run()
