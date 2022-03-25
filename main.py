import os
import uuid
import shutil
import subprocess
from flask import Flask, request, send_file
from spotify_dl.spotify import validate_spotify_url

app = Flask(__name__, static_folder='static', static_url_path='')

# serve static files
@app.route('/')
def homepage():
  return app.send_static_file('index.html')

# get songs given link
@app.route('/api/v1/getsongs', methods=['POST'])
def get_songs_api():

  # validate url
  if validate_spotify_url(request.json['link']):

    # create uuid
    file_uuid = str(uuid.uuid4())

    # call get_songs as subprocess
    subprocess.run(['python3', 'get_songs.py', request.json['link'], file_uuid])

    # get zipped file and setup as send_file
    res = send_file('archive/' + file_uuid + '.zip')

    # delete zip file
    os.remove('./archive/' + file_uuid + '.zip')

    # send zip to client
    return res

  # return error if url not vaildated
  return {'status': 'url invalid'}

# init
app.run(host='0.0.0.0')