import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import pprint




def songs(spotifyObject, searchQuery):
    user = spotifyObject.current_user()
    displayName = user['display_name']
    data_addition = []
    query = searchSong(spotifyObject, searchQuery)['tracks']
    for item in query['items']:
        '''pprint.pprint((item), width=1)
        print('\n\n\n')
        '''

        track = item
        song_id =('https://open.spotify.com/embed/track/'+str(track['id']))
        template = {"songLink": song_id, "name": track['name'], "songid": str(track['id']),
     "genre": "pop-rap", "author": track['artists'][0]['name'], "postedBy": displayName, "image": track['album']['images'][0]['url']}
        artists = []
        for i in track['artists']:
            artists.append(spotifyObject.search(track['artists'][0]['name'],limit=1,offset=0,type="artist"))
        for i in artists:
            follow_count = i['artists']['items'][0]['followers']['total']
            if follow_count <= 100000:
                data_addition.append(template)
                print(track['name'] + ' - ' + track['artists'][0]['name'])
                break        
    return(data_addition)

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
    userid = user["id"]
    followers = user['followers']['total']
    return displayName, userid

def searchSong(sp, searchQuery):
    '''max_ = False
    limit = 1
    while not max_:
        try:
            sp.search(q=searchQuery, type="track", limit=limit)
            limit += 1
        except:
            limit -= 1
            results = sp.search(q=searchQuery, type="track", limit=limit)
            max_ = True'''
    results = sp.search(q=searchQuery, type="track")
    '''for item in results["tracks"]["items"]:
        print(item["external_urls"])'''
    return results


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
