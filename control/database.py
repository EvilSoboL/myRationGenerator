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

        Return:
            tuple: id, category, name, description, portion, calories, protein, fat, carbohydrates, recipe
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

    def get_ingredients_id(self, dish_id: int) -> dict:
        """
        Метод, который возвращает словарь ингредиентов для определенного блюда.
        """
        with self.connection:
            self.cursor.execute(
                f"""
                SELECT ingredient, amount 
                FROM recipes
                WHERE dish_id = ?
                """,
                (dish_id,)
            )
            result = self.cursor.fetchall()
        result_dict = {row[0]: row[1] for row in result}
        return result_dict

    def get_ingredients_name_from_id(self, ingredients_ids: dict):
        """
        Метод, который возвращает имена ингредиентов по их id
        """
        ingredients_names = dict()
        for ingredients_id, amount in ingredients_ids.items():
            with self.connection:
                self.cursor.execute(
                    f"""
                    SELECT name 
                    FROM ingredients
                    WHERE id = ?
                    """,
                    (ingredients_id,)
                )
                result = self.cursor.fetchone()
                ingredients_names[result[0]] = amount
        return ingredients_names
