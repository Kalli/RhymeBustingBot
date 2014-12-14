import urllib2
import json 
import random
import os

apikey = os.environ.get('MUSIXMATCH_API_KEY')

def get_random_rap_lyrics(rapper):
    endpoint = "http://api.musixmatch.com/ws/1.1/"
    search_url = endpoint+"track.search?f_has_lyrics=1"
    search_url += "&f_artist_id=" + rapper["id"]
    search_url += "&apikey=" + apikey
    search = json.loads("".join(urllib2.urlopen(search_url).readlines()))
    try: 
        tracklist = search["message"]["body"]["track_list"]
        if tracklist and len(tracklist) > 0:
            track = random.choice(tracklist)["track"]
            rapper["track_share_url"] = track["track_share_url"]
            rapper["track_name"] = track["track_name"]
            track_url = endpoint + "track.lyrics.get?track_id="+str(track["track_id"])
            track_url += "&apikey=" + apikey
            lyrics  = json.loads("".join(urllib2.urlopen(track_url).readlines()))
            try: 
                rapper["lyrics"] = lyrics["message"]["body"]["lyrics"]["lyrics_body"]
            except KeyError:
                print "No lyrics found for "+rapper
    except KeyError:
        print "No tracks found for "+rapper
    return rapper




