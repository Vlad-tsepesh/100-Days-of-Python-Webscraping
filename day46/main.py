import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

from db.top_music_db import TopMusicDB
from scraper.music_scraper import MusicScraper

# date = input("Enter a date (YYYY-MM-DD): ")
# date = "2000-08-12"
# album_name = f"top-music-{date}"
album_name = "billboard-global-200"

music_scrape = MusicScraper(
    file_name=album_name,
    # url=f"https://www.billboard.com/charts/hot-100/{date}",
    url="https://www.billboard.com/charts/billboard-global-200/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
)

music_scrape.run()

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("SPOTIPY_USER_ID"),
    )
)
user_id = sp.current_user()["id"]

tracks_data = TopMusicDB(album_name).get_songs()

track_uris = []

for _, title, artist in tracks_data:
    query = f"track:{title} artist:{artist}"
    result = sp.search(q=query, type="track", limit=1)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
        print(f"✅ Found: {title} by {artist}")
    except IndexError:
        print(f"❌ Not found: {title} by {artist}")

playlist = sp.user_playlist_create(user=user_id, name=album_name, public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
