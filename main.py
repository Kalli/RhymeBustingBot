import musixmatch
import rhyming
import echonest
import time
import os
import traceback
import tweepy

CONSUMER_KEY = os.environ.get('RAP_BOT_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('RAP_BOT_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('RAP_BOT_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('RAP_BOT_ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def rappers_step_up_to_me():
    rapper1 = echonest.get_familiar_rapper()
    rapper2 = echonest.get_familiar_rapper()
    print rapper1["name"] + " vs. "+ rapper2["name"]
    print ""
    rapper1 = musixmatch.get_random_rap_lyrics(rapper1)
    rapper2 = musixmatch.get_random_rap_lyrics(rapper2)
    l1 = rapper1["lyrics"].split("\n")
    l2 = rapper2["lyrics"].split("\n")
    h = rhyming.find_rhymes(l1, l2)
    if h[0] > 0:
        tweettext = rapper1["name"] + ": " + l1[h[1]]
        tweettext += "\n"+rapper1["track_share_url"]
        api.update_status(tweettext)
        print tweettext
        tweettext = rapper2["name"] + ": " + l2[h[2]]
        tweettext += "\n"+rapper2["track_share_url"]
        api.update_status(tweettext)
        print tweettext
        print ""
    else: 
        print "No rhymes found "

while True:
    try:
        rappers_step_up_to_me()
    except Exception:
        print(traceback.format_exc())
    time.sleep(60 * 60) # I never sleep cause sleep is the cousin of death?
