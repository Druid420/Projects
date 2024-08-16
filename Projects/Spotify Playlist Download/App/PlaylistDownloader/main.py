import requests
from requests import *
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import time
from pynput import keyboard

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

#Use os to downlaod songs
def download_song(song_name, artist_name):
    command = f'ytmdl --nolocal --quiet "{song_name}" --artist "{artist_name}" --ignore-errors --format "m4a"'
    print (command)
    os.system(command)


def on_press(key):
    global stop_download #create global variable to stop download
    try:
        if key.char == 'q':
            stop_download = True # stop download when "q" pressed
            return False  # Stop listener
    except AttributeError:
        pass

# Global flag to stop the download
stop_download = False

songs = get_songs_spotify()
if songs:
    # Start the keyboard listener to listen for key press while loop runs
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    for song_name, artist_name in songs: #stops if key pressed or else proceeds
        if stop_download:
            break
        download_song(song_name, artist_name)
        time.sleep(0.5)

    listener.join()  # Ensure the listener thread finishes

print("Script ended.")

#add: downloads get zipped then user prompted to select download location