import os
import shutil
import threading
from dotenv import load_dotenv
from pydub import AudioSegment
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks, parse_spotify_url, validate_spotify_url
from spotify_dl.youtube import download_songs, default_filename

# setup spotify client
load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# get songs, call callback at end with uuid
def get_songs(request_url, uuid, cb):

  if validate_spotify_url(request_url):
    print(request_url)
    # parse url
    request_type, request_id = parse_spotify_url(request_url)
    
    # create new songs folder for new songs
    os.mkdir('./playlists/' + uuid)

    # get songs and put in ./uuid
    request_tracks = fetch_tracks(sp, request_type, request_url)

    # download_songs(request_tracks, './' + uuid, 'bestaudio/best', False)
    download_songs(request_tracks, './playlists/' + uuid, 'bestaudio/best', False)

    # build zip named uuid.zip
    shutil.make_archive('./archive/' + uuid, 'zip', './playlists/' + uuid)

    # delete songs
    shutil.rmtree('./playlists/' + uuid)

  return cb(uuid)