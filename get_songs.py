import os
import sys
import shutil
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks, parse_spotify_url
from spotify_dl.youtube import download_songs, default_filename

# setup spotify client
load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# get songs, call callback at end with uuid
def get_songs(request_url, uuid):

  # create destination folders if not exist
  if not os.path.isdir('playlists'):
    os.mkdir('./playlists')
  
  if not os.path.isdir('archive'):
    os.mkdir('archive')

  # parse url
  request_type, request_id = parse_spotify_url(request_url)
  
  # create new songs folder for new songs
  os.mkdir('./playlists/' + uuid)

  # get songs and put in ./uuid
  request_tracks = fetch_tracks(sp, request_type, request_url)

  # download tracks
  download_songs(request_tracks, './playlists/' + uuid, 'bestaudio/best', False)

  # build zip named uuid.zip
  shutil.make_archive('./archive/' + uuid, 'zip', './playlists/' + uuid)

  # delete songs
  shutil.rmtree('./playlists/' + uuid)

# get_songs gets called through a subprocess, and recieves arguments through the command line
get_songs(sys.argv[1], sys.argv[2])