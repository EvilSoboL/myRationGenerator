from controllers.database import DatabaseHandler

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

        self.database = DatabaseHandler()

    def get_random_dish(self, category):
        dish_info = self.database.get_random_dish(category)

