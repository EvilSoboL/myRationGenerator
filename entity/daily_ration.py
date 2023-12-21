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

    def get_union_ingredients(self):
        ingredients_dicts = [
            self.breakfast.ingredients,
            self.lunch.ingredients,
            self.dinner.ingredients,
            self.snack.ingredients
        ]
        union_ingredients_dicts = dict()
        for ingredients_dict in ingredients_dicts:
            for key, value in ingredients_dict.items():
                if key in union_ingredients_dicts:
                    union_ingredients_dicts[key] = union_ingredients_dicts[key] + " и " + value
                else:
                    union_ingredients_dicts[key] = value
        return union_ingredients_dicts
