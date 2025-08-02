from db.article_db import ArticleDB
from scraper.base_scraper import BaseScraper


class ArticleScraper(BaseScraper):
    def __init__(self, file_name, url):
        db_handler = ArticleDB()
        super().__init__(db_handler, file_name, url)

    def parse_data(self):
        title_tags = self.soup.find_all(name="span", class_="titleline")
        upvote_tags = self.soup.find_all(name="span", class_="score")

        titles = [tag.get_text() for tag in title_tags]
        links = [tag.find("a")["href"] for tag in title_tags]
        upvotes = [int(score.get_text().split()[0]) for score in upvote_tags]

        articles = {
            titles[i]: [
                links[i] if i < len(links) else None,
                upvotes[i] if i < len(upvotes) else 0
            ]
            for i in range(len(titles))
        }

        return dict(sorted(articles.items(), key=lambda item: item[1][1], reverse=True))

    def save_to_db(self, data):
        for title, (link, upvotes) in data.items():
            self.db_handler.insert_article(title, link, upvotes)
