import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprint import pprint

billboard_url = "https://www.billboard.com/charts/hot-100/"

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
# client_id = "541605efcddd4096a6ff07e22fa4ad6a"
# client_secret = "de44dd2f40b3415296ccc96c12ec7ec3"

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(f"{billboard_url}{date_input}")

response = requests.get(url=billboard_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

row_containers = soup.find_all(name="div", class_="o-chart-results-list-row-container")

song_titles = []
for row in row_containers:
    title = row.find(name="h3", id="title-of-a-story")
    song_titles.append(title.getText().strip())

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

playlist_name = f"{date_input} Billboard 100"
user_id = sp.current_user()["id"]
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

tracks = []
for title in song_titles:
    query = f"remaster track:{title} year:{date_input.split('-')[0]}"
    results = sp.search(q=query, limit=1)
    try:
        tracks.append(results["tracks"]["items"][0]["id"])
    except:
        print(f"{title} is not found!")

if len(tracks) > 0:
    sp.user_playlist_add_tracks(user=user_id, playlist_id=new_playlist["id"], tracks=tracks)
