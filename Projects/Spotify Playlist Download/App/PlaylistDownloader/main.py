import requests
from requests import *
import json
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load env file
load_dotenv()

def get_songs_spotify():
    # Authentication. Gets required ids from .env file. Also assign scope (intention of the program needed for API)
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    scope = "user-library-read"
    
    # Split link and find playlist id
    userPlaylist = input("Enter the link to your playlist: ")
    split = userPlaylist.split('/playlist/')
    playlist_id = split[1].split('?si')[0]

    # Authenticate and get access token for headers
    sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri="https://open.spotify.com/")
    token_info = sp_oauth.get_access_token()
    access_token = token_info['access_token']
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make a GET request to the Spotify API to get user's playlist
    response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=headers)

    # response.json() opens the response in json format so can be easily traversed
    data = response.json()
    # Gets different "items" meaning tracks from the data
    items = data["items"]
    songs = []

    # Appends all songs within the playlist to songs list
    # Then prints the songs. They are numbered starting at 1.
    for i, item in enumerate(items, 1):
        track = item["track"]
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]  # Get the first artist's name
        songs.append((song_name, artist_name))
        print(f"{i}: {song_name} by {artist_name}")
    return songs

def download_song(song_name, artist_name):
    command = f"ytmdl --nolocal --quiet '{song_name}' --artist '{artist_name}'"
    os.system(command)


songs = get_songs_spotify()
if songs:
    for song_name, artist_name in songs:
        download_song(song_name, artist_name)


#add way to stop thing