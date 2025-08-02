from db.base_db import BaseDB


class ArticleDB(BaseDB):
    def __init__(self, db_file="articles.db"):
        super().__init__(db_file)

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                title TEXT PRIMARY KEY,
                link TEXT,
                upvotes INTEGER
            )
        """)
        self.conn.commit()

    def insert_article(self, title, link, upvotes):
        self.cursor.execute("""
            INSERT OR REPLACE INTO articles (title, link, upvotes)
            VALUES (?, ?, ?)
        """, (title, link, upvotes))
        self.conn.commit()
