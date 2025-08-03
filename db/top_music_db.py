from db.base_db import BaseDB


class TopMusicDB(BaseDB):
    def __init__(self, db_file="top_music"):
        super().__init__(db_file)

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS music (
                ID INTEGER PRIMARY KEY,
                artist TEXT,
                song TEXT
            )
        """)
        self.conn.commit()

    def insert_data(self, id, artist, song):
        self.cursor.execute("""
            INSERT OR REPLACE INTO music (ID, artist, song)
            VALUES (?, ?, ?)
        """, (id, artist, song))
        self.conn.commit()

    def delete_song(self, id):
        self.cursor.execute("""
            DELETE FROM music
            WHERE ID = ?
        """, (id,))
        self.conn.commit()