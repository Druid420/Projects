import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
from getSongNames import getSongNames


load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
scope = 'playlist-modify-public' 
username = '31zxspvtemgw2yenenmxiquywwnm'
token = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost/', scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create the playlist
# ToDo: chnage this
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

songs = getSongNames()
list_of_song_uris = []
for song in songs:
  #Make search then get song uri from spotify
  result = spotifyObject.search(q=song)
  list_of_song_uris.append(result['tracks']['items'][0]['uri'])

#Find new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# Add songs
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist, tracks=list_of_song_uris)
print("Done!")