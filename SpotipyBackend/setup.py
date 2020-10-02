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
def run():
    import os
    import sys
    import json
    import spotipy
    import webbrowser
    import spotipy.util as util
    from json.decoder import JSONDecodeError

    # Get the username from terminal
    #https://open.spotify.com/user/yv5v7ustl0gvj2ismb6ru1bk1?si=L5gHBWM8RPqsh8yps34BfQ
    #https://open.spotify.com/user/yv5v7ustl0gvj2ismb6ru1bk1?si=T5eiCgtSTyiGmEdpF8MWbg
    username = "yv5v7ustl0gvj2ismb6ru1bk1?si=L5gHBWM8RPqsh8yps34BfQ"
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

    # Erase cache and prompt for user permission
    try:
        token = util.prompt_for_user_token(username, scope) # add scope
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope) # add scope

    # Create our spotify object with permissions
    spotifyObject = spotipy.Spotify(auth=token)
    #print(spotifyObject.me())
    return spotifyObject
