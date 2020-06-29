import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from datetime import date, time, datetime, timedelta
import json
import sp_config
import sk_config

#Get top Spotify artists
def get_top_artists():
    username = sp_config.username
    scope = sp_config.scope
    token = util.prompt_for_user_token(username,
                            scope,
                            client_id=sp_config.client_id,
                            client_secret=sp_config.client_secret,
                            redirect_uri=sp_config.redirect_uri)
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
def get_upcoming_concerts():
    current_date =  date.today()
    max_date = current_date + timedelta(90)
    metro_area_id = sk_config.metro_area_id # Austin: 9179, San Antonio: 7554, Dallas: 35129
    api_key = sk_config.api_key 

    #API Request for getting metro_area_id
    #metro_response = requests.get("https://api.songkick.com/api/3.0/search/locations.json?query='Austin'&apikey={apikey}")
    
    count = 0
    page = 1
    for page in range (1,4):
        metro_uri ='https://api.songkick.com/api/3.0/metro_areas/' + metro_area_id + '/calendar.json?apikey=' \
                + api_key + '&min_date=' + str(current_date) + '&max_date=' + str(max_date) + '&page=' + str(page)

        events_response = requests.get(metro_uri)

        r_dict = events_response.json()

        for i in r_dict['resultsPage']['results']['event']:
            for j in i['performance']:
                print(j['artist']['displayName'])

#Main Function
if __name__ == "__main__":
    # top_artists = get_top_artists()
    get_upcoming_concerts()

