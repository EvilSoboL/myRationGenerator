import sqlite3

from config import PATH_TO_DB


class DatabaseHandler:
    def __init__(self):
        self.path_to_db = PATH_TO_DB
        self.connection = None
        self.cursor = None

        self.connect_to_db()

    def connect_to_db(self):
        self.connection = sqlite3.connect(self.path_to_db)
        self.cursor = self.connection.cursor()

    def insert_into_experiments(self):
        with self.connection:
            self.cursor.execute()

    def get_unique_fuels_in_experiments(self) -> int:
        """
        Метод, который возвращает количество уникальных fuel_id в таблице experiment.
        """
        with self.connection:
            self.cursor.execute(
                """
                SELECT COUNT(DISTINCT fuel_id) AS unique_fuels_count FROM "main"."experiments"
                """
            )
            result = self.cursor.fetchone()[0]
        return result

