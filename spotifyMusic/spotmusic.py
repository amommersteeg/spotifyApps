#!/usr/bin/env python3

# https://github.com/plamere/spotipy
# source ./bin/activate


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import pprint
import json

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="86e129aab6334e4e9df9",
                                               client_secret="a97c6e3f89524352bbca659941",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))


with open('music.json') as f:
    data = json.load(f)


# Read json file, from offset and for x number of items
# Search for track, use track name and artist from json, return 20 items
# double check artist, track, album, loop through all items until all three match. 
# if found add id to trackToAdd array -> save to json file 
# if not found add object with {title, artist, album} to tracksSkip array -> save to file
# upload files to saved tracks

tracksAdd = []
trackIds = []
tracksSkip = []

def copyMusic(data, start, limit):
    reverseNum = -(len(data) - start)
    data2 = data[reverseNum:]
    for track in data2[:limit]:
        query = track['title'] + " " + track['artists'][0]['name']
        results = sp.search(query, 10, 0, "track", "CA")
        isFound = False
        for item in results['tracks']['items']:
            if(track['title'] == item['name'] and track['artists'][0]['name'] == item['artists'][0]['name']):
                tracksAdd.append({"name": track['title'], "artists": item['artists'][0]['name'], "album": track['album']['name'], "id":item['id']})
                trackIds.append(item['id'])
                isFound = True
                if len(trackIds) == 10:
                    sp.current_user_saved_tracks_add(trackIds)
                    trackIds.clear()
                break

        if isFound is not True:
            tracksSkip.append({"name": track['title'], "artists": track['artists'][0]['name'], "album": track['album']['name']})


copyMusic(data, 9, 1000)

if len(trackIds) > 0:
    sp.current_user_saved_tracks_add(trackIds)
    trackIds.clear()

with open('tracksAdd.json') as f:
    data = json.load(f)
    data.append(tracksAdd)
    with open('tracksAdd.json', 'w') as outfile:
        json.dump(data, outfile)

if len(tracksSkip) > 0:
    with open('tracksSkip.json') as f:
        data = json.load(f)
        data.append(tracksSkip)
        with open('tracksSkip.json', 'w') as outfile:
            json.dump(data, outfile)

print("Spotify copying complete!!")

