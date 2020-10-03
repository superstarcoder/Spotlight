"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
"""
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import pprint

# Get the username from terminal
#https://open.spotify.com/user/yv5v7ustl0gvj2ismb6ru1bk1?si=L5gHBWM8RPqsh8yps34BfQ
username = "yv5v7ustl0gvj2ismb6ru1bk1?si=L5gHBWM8RPqsh8yps34BfQ"
scope = 'user-read-private user-read-playback-state user-modify-playback-state user-library-read'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)
print(spotifyObject.me())

# Get current device
#devices = spotifyObject.devices()
#deviceID = devices['devices'][0]['id']

# Current track information
#track = spotifyObject.current_user_playing_track()
#artist = track['item']['artists'][0]['name']
#track = track['item']['name']

#if artist != "":
#    print("Currently playing " + artist + " - " + track)

# User information
    user = spotifyObject.current_user()
    displayName = user['display_name']
    followers = user['followers']['total']

# Loop
while True:
    # Main Menu
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")

        # Artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        try:
            print(artist['genres'][0])
        except IndexError:
            print("genre name not available")
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        print(artistID)

        fellow_artists_data = (spotifyObject.artist_related_artists(artistID))

        for i in fellow_artists_data['artists']:
            print(i['name'])
        
        print()

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        # See album art
        while True:
            songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID, None, trackSelectionList) # added
            webbrowser.open(trackArt[int(songSelection)])

    if choice == "1":
        break

    # print(json.dumps(trackResults, sort_keys=True, indent=4))
