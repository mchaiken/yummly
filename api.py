import urllib2
import json

def getResults(ingredients):
    url="""
    http://api.yummly.com/v1/api/recipes?_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"""
    for ingredient in ingredients:
        url+="&allowedIngredient[]="+ingredient
    print url
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    results=d["matches"]
    return results

getResults(["chocolate","vanilla","sugar"])


