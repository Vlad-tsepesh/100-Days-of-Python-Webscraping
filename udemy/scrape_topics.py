from bs4 import BeautifulSoup

from fh.file_handler import FileHandler

html = FileHandler().load_html("udemy")
soup = BeautifulSoup(html, "html.parser")
print(soup.text)