import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from datetime import date, time, datetime, timedelta
import json

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
    current_date =  date.today()
    max_date = current_date + timedelta(90)
    metro_area_id = '9179' # Austin: 9179, San Antonio: 7554, Dallas: 35129
    songkick_api_key = 'X4adldhma4pF3yAI'

    #API Request for getting metro_area_id
    #metro_response = requests.get("https://api.songkick.com/api/3.0/search/locations.json?query='Austin'&apikey={apikey}")
    
    count = 0
    page = 1
    for page in range (1,4):
        metro_uri ='https://api.songkick.com/api/3.0/metro_areas/' + metro_area_id + '/calendar.json?apikey=' \
                + songkick_api_key + '&min_date=' + str(current_date) + '&max_date=' + str(max_date) + '&page=' + str(page)

        events_response = requests.get(metro_uri)

        r_dict = events_response.json()

        for i in r_dict['resultsPage']['results']['event']:
            for j in i['performance']:
                print(j['artist']['displayName'])

#Main Function
if __name__ == "__main__":
    # top_artists = get_top_artists()
    get_upcoming_concerts()

