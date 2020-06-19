import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

username = 'silvertone31'

scope = 'user-top-read'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id='184650a74ff247dbb521d6236247b105',
                           client_secret='583e43282a7e4016b7e9f90c5fd61e51',
                           redirect_uri='http://localhost:8888/callback')

top_artists = []
#Get top 20 artists in three ranges without duplicates
if token:
    sp = spotipy.Spotify(auth=token)
    for sp_range in ['short_term', 'medium_term', 'long_term']:
        results = sp.current_user_top_artists(time_range=sp_range, limit=20)
        for item in results['items']:
            if (item['name'] not in top_artists):
                top_artists.append(item['name'])

    print(top_artists)
    print(len(top_artists))
else:
    print("Can't get token for", username)



    

