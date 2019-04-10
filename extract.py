###Search Audio API EXAMPLE###

# search_url_audio = "https://api.spotify.com/v1/audio-features/"
# audio_url = search_url_audio + "59PYgzOiOjGDzjDT5N5oOX"

# audio_json = requests.get(audio_url, headers = token_headers).json()

import os
import time
import requests
import numpy as np
import pandas as pd
from requests.auth import HTTPBasicAuth
from client import client_id, client_secret

## Make directory for CSV files 

# path = "Top Country CSV"

# try:  
#     os.mkdir(path)

# except OSError:  
#     print ("Creation of the directory %s failed" % path)
    
# else:  
#     print ("Successfully created the directory %s " % path)

## Top 50 Playlist by Country Excel
top50_playlist_df = pd.read_excel("Resources/Top50_Playlist_by_Country.xlsm")

## This request grants us a temporary token to use to access the json data from spotify.
token_url = "https://accounts.spotify.com/api/token"
headers = {'content-type': 'application/x-www-form-urlencoded'}

token_params = {"grant_type" : "client_credentials"}

token_json = requests.post(token_url, params = token_params, headers = headers, auth = (client_id, client_secret)).json()
token = token_json['access_token']

# Required header to access spotify api
token_headers = {'authorization': f"Bearer {token}"}

# Counter is used to grab country name from top50_playlist_df
counter = 0

# Search api endpoint for playlist and audio features
search_url_playlist = "https://api.spotify.com/v1/playlists/"
search_url_audio = "https://api.spotify.com/v1/audio-features/"

print("--------------------------\nBegin Exporting CSV Files\n--------------------------")

# Loops through each playlist ID from top50_playlist_df
for playlist_id in top50_playlist_df["Spotify Playlist ID"]:
    
    playlist_url = search_url_playlist + playlist_id
    
    # Store entire playlist json data into variable
    playlist_json = requests.get(playlist_url, headers = token_headers).json()
    
    # List to store json data
    artist_name = []
    artist_id = []
    track_name = []
    track_id = []
    release_date = []
    popularity = []
    danceability = []
    energy = []
    
    # Number of tracks within each playlist (should be 50 songs)
    number_of_tracks = len(playlist_json["tracks"]["items"])
    
    # Loops through each playlist in playlist_json
    for i in range(number_of_tracks):
        time.sleep(0.02)
        
        try:
            # Store track json as variable for faster access
            playlist_tracks = playlist_json["tracks"]["items"][i]["track"]
            
            # Append artist name, artist ID, track name, track ID, release date, and popularity
            artist_name.append(playlist_tracks["album"]["artists"][0]["name"])
            artist_id.append(playlist_tracks["album"]["artists"][0]["id"])
            track_name.append(playlist_tracks["name"])
            
            # Store track ID as variable for faster access
            track_ids = playlist_tracks["id"]
            track_id.append(track_ids)
            
            release_date.append(playlist_tracks["album"]["release_date"])
            popularity.append(playlist_tracks["popularity"])
            
            # Accessing audio endpoint from spotify
            audio_url = search_url_audio + track_ids

            audio_json = requests.get(audio_url, headers = token_headers).json()
            
            # Append danceability and energy score
            danceability.append(audio_json["danceability"])
            energy.append(audio_json["energy"])
            
        except (KeyError, IndexError):
            danceability.append("NaN")
            energy.append("NaN")
            
            print(f"Could not find audio ID | {track_ids}")
    
    #Create DataFrame to store into excel
    artist_country_df = pd.DataFrame({"Artists Name" : artist_name,
                                      "Artist ID" : artist_id,
                                      "Track Name" : track_name,
                                      "Track ID" : track_id,
                                      "Release Date" : release_date,
                                      "Popularity" : popularity,
                                      "Danceability" : danceability,
                                      "Energy" : energy})
    
    # Country Name
    country = top50_playlist_df["Country"][counter]
    
    # Export dataframe of each country into seperate excel files
    #artist_country_df.to_csv(f"Top Country CSV/{country}_top_50.csv")
    
    counter += 1
    
print("--------------------------\nDone Exporting CSV Files\n--------------------------")