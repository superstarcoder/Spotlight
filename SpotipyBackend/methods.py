import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError




def currentlyPlaying(spotifyObject):
    # Get current device
    devices = spotifyObject.devices()
    try:
        deviceID = devices['devices'][0]['id']
        track = spotifyObject.current_user_playing_track()
        artist = track['item']['artists'][0]['name']
        track = track['item']['name']
    except: #if nothing is currently playing
        print("nothing is currently playing")
        return
    

    # Current track information

    if artist != "":
        print("Currently playing " + artist + " - " + track)
    return artist, track

def userInfo(spotifyObject):
    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']
    followers = user['followers']['total']
    return displayName

def searchSong(sp, searchQuery):
    results = sp.search(q=searchQuery, type="track", limit=10)
    for item in results["tracks"]["items"]:
        print(item["external_urls"])
    #return results


def searchArtist(spotifyObject, searchQuery):
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

    return albumResults
