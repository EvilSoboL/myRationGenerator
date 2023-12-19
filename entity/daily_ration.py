from entity.dish import Dish


class DailyRation:
    def __init__(self):
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        self.snack = None

    def get_daily_ration(self):
        self.breakfast = Dish()
        self.lunch = Dish()
        self.dinner = Dish()
        self.snack = Dish()
        
        self.breakfast.get_random_dish('Завтрак')
        self.lunch.get_random_dish('Основные блюда')
        self.dinner.get_random_dish('Основные блюда')
        self.snack.get_random_dish('Салаты')
