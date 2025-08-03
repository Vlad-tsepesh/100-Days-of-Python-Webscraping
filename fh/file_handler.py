import requests

from fh.path_manager import PathManager


class FileHandler:
    def __init__(self):
        self.html: str = ""
        self.path = PathManager()

    def get_html(self, url: str, file_name: str, headers) -> bool:
        path = self.path.get_data_path(file_name)
        if path.exists():
            return False
        response = requests.get(url, headers)
        response.raise_for_status()  # Good practice to catch HTTP errors
        self.html = response.text
        return True

    def save_html(self, file_name: str) -> None:
        if not self.html:
            raise ValueError("No HTML content to save. Call get_html() first.")
        path = self.path.get_data_path(file_name)
        with open(path, "w", encoding="utf-8") as file:
            file.write(self.html)

    def load_html(self, file_name: str) -> str:
        path = self.path.get_data_path(file_name)
        with open(path, "r", encoding="utf-8") as file:
            self.html = file.read()
        return self.html
