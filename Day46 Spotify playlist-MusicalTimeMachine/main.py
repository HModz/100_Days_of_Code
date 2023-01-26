import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want do travel to? (YYYY-MM-DD): ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=url)
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

titles_headers = soup.select("li h3")
titles = [title.getText().strip() for title in titles_headers]

print(titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="***",
                                               client_secret="***",
                                               redirect_uri="***",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
