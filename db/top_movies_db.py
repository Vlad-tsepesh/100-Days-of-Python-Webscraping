from db.base_db import BaseDB


class TopMoviesDB(BaseDB):
    def __init__(self, db_file="topmovies.db"):
        super().__init__(db_file)

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS top_movies (
                ID INTEGER PRIMARY KEY,
                Movies TEXT
            )
        """)
        self.conn.commit()

    def insert_movies(self, id, movie):
        self.cursor.execute("""
            INSERT OR REPLACE INTO top_movies (ID, movies)
            VALUES (?, ?)
        """, (id, movie))
        self.conn.commit()

    def delete_movie(self, id):
        self.cursor.execute("""
            DELETE FROM top_movies
            WHERE ID = ?
        """, (id,))
        self.conn.commit()
