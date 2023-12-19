from control.database import DatabaseHandler


class Dish:
    def __init__(self):
        self.id = None
        self.category = None
        self.name = None
        self.description = None
        self.portion = None
        self.calories = None
        self.protein = None
        self.fat = None
        self.carbohydrates = None
        self.recipe = None

        self.ingredients = None

        self.database = DatabaseHandler()

    def get_random_dish(self, category: str) -> None:
        """
        Возвращает случайное блюдо из выбранной категории.
        Список категорий:
        Завтрак, Бульон, Закуски, Основные блюда, Паста и пицца, Салаты.
        """
        dish_info = self.database.get_random_dish(category)
        self.id = dish_info[0]
        self.category = dish_info[1]
        self.name = dish_info[2]
        self.description = dish_info[3]
        self.portion = dish_info[4]
        self.calories = dish_info[5]
        self.protein = dish_info[6]
        self.fat = dish_info[7]
        self.carbohydrates = dish_info[8]
        self.recipe = dish_info[9]

        id_dict = self.database.get_ingredients_id(self.id)
        ingredient_dict = self.database.get_ingredients_name_from_id(id_dict)

        self.ingredients = ingredient_dict
