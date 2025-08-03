from db.top_music_db import TopMusicDB
from scraper.base_scraper import BaseScraper


class MusicScraper(BaseScraper):
    def __init__(self, file_name, url, headers):
        db_handler = TopMusicDB(file_name)
        super().__init__(db_handler, file_name, url, headers)
        self.pattern = r'^(\d+)[):]\s*(.+)'

    def parse_data(self):
        title_tags = self.soup.find_all(class_="o-chart-results-list-row")
        return [(line.strip() for line in song.text.split("LW")[0].splitlines() if line.strip() and not "NEW" in line) for
          song in title_tags]

    def save_to_db(self, data):
        for number, song, artist in data:
            self.db_handler.insert_data(number, artist, song)
