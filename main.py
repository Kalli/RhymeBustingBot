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
    success = False
    rapper1 = echonest.get_familiar_rapper()
    rapper2 = echonest.get_familiar_rapper()
    print ""
    print rapper1["name"] + " vs. "+ rapper2["name"]
    rapper1 = musixmatch.get_random_rap_lyrics(rapper1)
    rapper2 = musixmatch.get_random_rap_lyrics(rapper2)
    if "lyrics" in rapper1 and "lyrics" in rapper2:
        rapper1["lyrics"] = rapper1["lyrics"].split("\n")
        rapper2["lyrics"] = rapper2["lyrics"].split("\n")
        rhyme = rhyming.find_rhymes(rapper1["lyrics"], rapper2["lyrics"])
        if rhyme[0] > 0:
            tweet_lyrics(rapper1, rapper2, rhyme)
            success = True
        else: 
            print "No rhymes found"
    else: 
        print "No lyrics found"
    return success

def tweet_lyrics(rapper1, rapper2, rhyme):
    tweet1 = rapper1["name"] + ": " + rapper1["lyrics"][rhyme[1]]
    tweet2 = rapper2["name"] + ": " + rapper2["lyrics"][rhyme[2]]
    print tweet1
    print tweet2
    tweet1 += "\n" +rapper1["track_share_url"] 
    tweet2 += "\n" +rapper2["track_share_url"] 
    tweetid = api.update_status(tweet1).id_str
    api.update_status(tweet2, tweetid).id_str

while True:
    try:
        success = rappers_step_up_to_me()
        time.sleep(20) 
        if success:
            time.sleep(60*60) 
        else:
            time.sleep(60)
    except Exception:
        print(traceback.format_exc())
