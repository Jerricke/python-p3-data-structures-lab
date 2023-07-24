spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    result = list()
    for food in spicy_foods:
        result.append(food.get("name"))
    return result
    pass

def get_spiciest_foods(spicy_foods):
    result = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            result.append(food)
    return result
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"], end=" ")
        print("("+food["cuisine"]+ ") |", end=" ")
        print("Heat Level: "+food["heat_level"]*"🌶")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(food["name"], end=" ")
            print("("+food["cuisine"]+ ") |", end=" ")
            print("Heat Level: "+food["heat_level"]*"🌶")
    pass

def get_average_heat_level(spicy_foods):
    heat = list()
    for food in spicy_foods:
        heat.append(food["heat_level"])
    return sum(heat)/len(heat)
    pass

import ipdb

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
