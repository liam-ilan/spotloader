import shutil
import os
import uuid
from flask import Flask, request, send_file
from get_songs import get_songs

app = Flask(__name__, static_folder='static', static_url_path='')

# serve static files
@app.route('/')
def homepage():
  return app.send_static_file('index.html')

# api - get songs given link
@app.route('/api/v1/getsongs', methods=['POST'])
def get_songs_api():

  # callback when download is finished
  def cb(file_uuid):

    # get file
    res = send_file('./archive/' + file_uuid + '.zip')

    # delete file
    os.remove('./archive/' + file_uuid + '.zip')

    # return (will be sent to client)
    return res

  # returns whatever callback returns, input validated in function
  return get_songs(request.json['link'], str(uuid.uuid4()), cb)

# init
app.run(host='0.0.0.0')