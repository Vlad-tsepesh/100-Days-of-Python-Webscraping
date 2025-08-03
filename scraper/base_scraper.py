from bs4 import BeautifulSoup

from fh.file_handler import FileHandler


class BaseScraper:
    def __init__(self, db_handler, file_name, url, headers=""):
        self.file_handler = FileHandler()
        self.db_handler = db_handler
        self.file_name = file_name
        self.url = url
        self.headers = headers
        self.soup = None

    def get_and_save_html(self):
        if self.file_handler.get_html(self.url, self.file_name,self.headers):
            self.file_handler.save_html(self.file_name)

    def load_html(self):
        html = self.file_handler.load_html(self.file_name)
        self.soup = BeautifulSoup(html, "html.parser")

    def parse_data(self):
        """Override in subclass: parse self.soup and return data"""
        raise NotImplementedError

    def save_to_db(self, data):
        """Override or provide generic DB saving"""
        raise NotImplementedError

    def run(self):
        self.get_and_save_html()
        self.load_html()
        data = self.parse_data()
        self.save_to_db(data)
        self.db_handler.close()
