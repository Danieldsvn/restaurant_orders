from models.dish import Dish
from models.ingredient import Ingredient
import csv


def get_dishes_from_csv(path):
    with open(path, encoding="utf8") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        dishes = {}
        for index, item in enumerate(data):
            if index > 0:
                if item[0] in dishes:
                    dishes[item[0]]["ingredients"].append(
                        (item[2], int(item[3]))
                    )
                else:
                    dishes[item[0]] = {}
                    dishes[item[0]]["price"] = float(item[1])
                    dishes[item[0]]["ingredients"] = []
                    dishes[item[0]]["ingredients"].append(
                        (item[2], int(item[3]))
                    )

        return dishes


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.get_dishes(source_path)

    def get_dishes(self, path):
        dishes_dictionary = get_dishes_from_csv(path)
        dishes_set = set()

        for dish_name in dishes_dictionary:
            dish = Dish(dish_name, dishes_dictionary[dish_name]["price"])
            for ingredient, qty in dishes_dictionary[dish_name]["ingredients"]:
                ingredient_instance = Ingredient(ingredient)
                dish.add_ingredient_dependency(ingredient_instance, qty)
            dishes_set.add(dish)

        return dishes_set
