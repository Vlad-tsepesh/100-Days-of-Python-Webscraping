from scraper.music_scraper import MusicScraper

# date = input("Enter a date (YYYY-MM-DD): ")
date = "2020-08-12"

music_scrape = MusicScraper(
    file_name=f"top-music-{date}",
    url=f"https://www.billboard.com/charts/hot-100/{date}",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
)

music_scrape.run()

