from db.base_db import BaseDB


class RentalDB(BaseDB):
    def __init__(self, db_file, table_name):
        self.table_name = table_name
        super().__init__(db_file)

    def _create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                ID INTEGER PRIMARY KEY,
                price INTEGER,
                address TEXT,
                link TEXT
            )
        """)
        self.conn.commit()

    def insert_data(self, id, price, address, link):
        self.cursor.execute(f"""
            INSERT OR REPLACE INTO {self.table_name} (ID, price, address, link)
            VALUES (?, ?, ?, ?)
        """, (id, price, address, link,))
        self.conn.commit()

    def delete_song(self, id):
        self.cursor.execute(f"""
            DELETE FROM {self.table_name}
            WHERE ID = ?
        """, (id,))
        self.conn.commit()

    def get_data(self):
        self.cursor.execute(f"""
            SELECT * FROM {self.table_name}
        """)
        return self.cursor.fetchall()


