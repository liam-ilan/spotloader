# SpotLoader
## Download Spotify Playlists
https://spotloader.snowboardsheep.repl.co/

### About
Spotloader downloads songs from spotify playlists. Songs are returned in mp3 format, and are zipped for personal use.

### API
Spotloader can download songs without the web client.

Simply make a `POST` request to `https://spotloader.snowboardsheep.repl.co/api/v1/getsongs`
- Gets `{"link": "Link to spotify playlist"}`
- Returns `.zip` containing `.mp3` files of songs in playlist
- On error, returns `{"status": "url invalid"}`

### Development
Clone this repo
```
git clone https://github.com/liam-ilan/spotloader.git
```

Install packages
```
pip install -r requirements.txt
``` 

Create a .env file with the following contents
```
SPOTIPY_CLIENT_ID="Spotify Client ID Here"
SPOTIPY_CLIENT_SECRET="Spotify Client Secret Here"
```
Credentials can be obtained from the Spotify developer dashboard.

Start up the web server
```
python main.py
```

Happy developing!

### Hosting
This project is hosted on https://replit.com, you can find it at https://replit.com/@snowboardsheep/spotloader.

### Credit
Created by [Liam Ilan](https://liamilan.com)
Built using https://github.com/SathyaBhat/spotify-dl and https://github.com/plamere/spotipy.