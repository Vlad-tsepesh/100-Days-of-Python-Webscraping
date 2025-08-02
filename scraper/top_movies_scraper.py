import re

from db.top_movies_db import TopMoviesDB
from fh.file_handler import FileHandler
from scraper.base_scraper import BaseScraper


class TopMoviesScraper(BaseScraper):
    def __init__(self, file_name, url):
        db_handler = TopMoviesDB()
        super().__init__(db_handler, file_name, url)
        self.pattern = r'^(\d+)[):]\s*(.+)'

    def parse_data(self):
        title_tags = self.soup.find_all(name="h3", class_="title")
        cleaned = [' '.join(tag.text.split()) for tag in title_tags]
        extracted = []
        for title in cleaned:
            match = re.match(self.pattern, title)
            if match:
                extracted.append((match.group(1), match.group(2)))
        return extracted

    def save_to_db(self, data):
        for number, title in data:
            self.db_handler.insert_movies(number, title)
