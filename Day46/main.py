"""playlist timecapsule"""
import os
import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIFY_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]

TRAVEL_DATE = "2015-01-25"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
# first scrape the billboard top 100 songs from the specific date
response = requests.get(
    f"{BILLBOARD_URL}{TRAVEL_DATE}",
    timeout=5,
)
soup = bs4.BeautifulSoup(response.text, "html.parser")

# first, extract the song list
song_list = []
song_names = soup.select(selector="li h3", class_="c-title")

for song in song_names:
    text = song.getText().strip()
    song_list.append(text)

# first 100 matches are the song titles
song_list = song_list[0:100]


# connect to spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-modify-private playlist-read-private user-read-recently-played",
        cache_path="token.txt",
    )
)


# Get current user details
user = sp.current_user()
# print(user)
user_id = user["id"]

# get song URLs:
track_ids = []
skipped_songs = []

# could improve the search function to be more specific with title + artist
for song in song_list:
    try:
        track_id = sp.search(q=f"track:{song}", type="track", limit=1)
        track_ids.append(track_id["tracks"]["items"][0]["uri"])
    except IndexError:
        skipped_songs.append(song)
        print(f"{song} not found in Spotify. Skipped.")
print(f"{len(skipped_songs)} were not found on Spotify.")

# finally, create a playlist with the songs
time_travel_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{TRAVEL_DATE} Billboard 100",
    public=False,
    collaborative=False,
    description=f"Billboard top 100 songs from {TRAVEL_DATE}",
)

time_travel_playlist_id = time_travel_playlist["id"]

# then add each song
sp.playlist_add_items(
    playlist_id=time_travel_playlist_id,
    items=track_ids,
    position=None,
)

print("done")
