#!/usr/bin/pyt
from ytmusicapi import YTMusic
import json
ytmusic = YTMusic('auth.json')
songs = ytmusic.get_library_songs(5000, False, 'recently_added')

with open('youtubeMusic.json', 'w') as fp:
    json.dump(songs, fp, indent=4)