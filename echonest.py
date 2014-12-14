from random import choice
import json
import urllib2
import os

apikey = os.environ.get('ECHONEST_API_KEY')

def get_rapper(sort):
    endpoint = "http://developer.echonest.com/"
    url = endpoint+ "api/v4/artist/search?format=json"
    url += "&api_key="+apikey
    url +="&bucket=id:musixmatch-WW&genre=rap&limit=true"
    url +="&sort="+sort
    url += "&results=100"
    response = json.loads("".join(urllib2.urlopen(url).readlines()))
    rapper = choice(response["response"]["artists"])
    musixmatch_id = rapper["foreign_ids"][0]["foreign_id"].replace("musixmatch-WW:artist:","")
    return {"name": rapper["name"], "id": musixmatch_id}


def get_familiar_rapper():
    return get_rapper("familiarity-desc")

def get_hott_rapper():
    return get_rapper("hotttnesss-desc")