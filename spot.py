import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

#Get top Spotify artists
def get_top_artists():
    username = 'silvertone31'
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username,
                            scope,
                            client_id='184650a74ff247dbb521d6236247b105',
                            client_secret='583e43282a7e4016b7e9f90c5fd61e51',
                            redirect_uri='http://localhost:8888/callback')
    top_artists = []
    
    if token:
        sp = spotipy.Spotify(auth=token)
        for sp_range in ['short_term', 'medium_term', 'long_term']:
            results = sp.current_user_top_artists(time_range=sp_range, limit=50)
            for item in results['items']:
                if (item['name'] not in top_artists):
                    top_artists.append(item['name'])
        return top_artists

    else:
        print("Can't get token for", username)
        return None


#Check for concerts for top artists
def get_upcoming_concerts(artists):
    # artists = artists

    response = requests.get('https://api.songkick.com/api/3.0/artists/379603/gigography.json?apikey=X4adldhma4pF3yAI')
    response.json()

    print(response.text)


#Main Function
if __name__ == "__main__":
    # get_upcoming_concerts(get_top_artists())
    get_upcoming_concerts(['Band of Horses', 'Incubus', 'The Killers'])

