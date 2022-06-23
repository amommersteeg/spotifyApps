# spotifyApps
Quick and dirty script to move liked songs from Youtube Music to Spotify. 

Takes advantage of [ytmusicapi](https://ytmusicapi.readthedocs.io/en/latest/) and [spotipy](https://spotipy.readthedocs.io/en/master/) libraries.

The ytmusic.py script create a json file with an array of songs from your Youtube music library. The spotmusic.py then takes the json file and searches Spotify for the equivalent song and likes it. If the song is liked it gets added to tracksAdd.json and if an equivalent song could not be found it adds it to tracksSkip.json. 

Equivalent songs are found based on track title and track artists. 

To use
1. Follow ytmusicapi instructions to create auth header and add to auth.json -> https://ytmusicapi.readthedocs.io/en/latest/setup.html
2. Run the ytmusic.py script to generate .json of all liked/library songs from Youtube music
3. Follow the spotipy instructions to create a client and secret and add to spotmusic.py -> https://github.com/plamere/spotipy#quick-start
4. Add the output from ytmusic.py relative to the spotmusic.py script
5. Run the spotmusic.py
