import urllib2, json, random

def getResults(ingredients):
    url="""
    http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"""
    for ingredient in ingredients:
        if ingredient[0]==" ":
            ingredient= ingredient[1:]
        url+="&allowedIngredient[]="+ingredient.lower()
    #print url
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    results=d["matches"]
    return results

#getResults(["chocolate","vanilla","sugar"])


def getRecipe(id):
    url="http://api.yummly.com/v1/api/recipe/"+id+"?_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"
    #print url
    request = urllib2.urlopen(url)
    result = request.read()
    #print url
    return json.loads(result)

#getRecipe("Chocolate-Mousse-Epicurious_1")

def getSong(tag):
    url="http://8tracks.com/mix_sets/tags:"+tag.lower()+".json?api_key=52947991b38f982d9dc6842c0bd653fcd0df0a20&include=mixes"
    print url
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    index=random.randrange(0,10)
    if index >= len(d["mixes"]):
        index = len(d["mixes"]) -1
    if index == -1:
        url= getSong("cooking")
    else:    
        url=d["mixes"][index]["restful_url"]
    return url
    #print getSong("Halloween")


def getVideo(dish):
    dish="+".join(dish.split(" "))
    url="https://gdata.youtube.com/feeds/api/videos?q="+dish+"&oderby=viewCount&alt=json&key=AI39si6RrkEc9vwqZLhttr2enr_FjqalFmXQJuKqY6ix6FC0SaPu17-tlmpopY5u44-5T5YkIbuFRKlQSIDnGHfY6H1Qx-69Ig"
    request= urllib2.urlopen(url)
    result=request.read()
    x=json.loads(result)
    yvideo=x["feed"]["entry"][0]["link"][0]["href"][32:43]
    print "URL ://www.youtube.com/embed/"+yvideo
    return "//www.youtube.com/embed/"+yvideo
   

getVideo("chocolate cake")
