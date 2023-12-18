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

    def get_random_dish(self, category: str) -> tuple:
        """
        Возвращает случайное блюдо из выбранной категории.
        Список категорий:
        Завтрак, Бульон, Закуски, Основные блюда, Паста и пицца, Салаты
        """
        with self.connection:
            self.cursor.execute(
                f"""
                SELECT * 
                FROM dishes
                WHERE category = ? 
                ORDER BY RANDOM() 
                LIMIT 1
                """,
                (category,)
            )
            result = self.cursor.fetchone()
        return result

    def get_ingredients(self, dish_id):
        """
        Метод, который возвращает список ингредиентов для определенного блюда.
        """
        pass