"""
recipe handles multiple recipes

Class included: Recipe

NAME: Jaihui Zhou
SEMESTER: 2023 Spring
"""
import csv


class Recipe:
    """
    Class: Recipe
    Attributes: short_name, ingredients, details
    Methods: check_ingredients, add_ingredient,
    remove_ingredient, __str__
    """
    # list is used for ingredients, because it may be edited in the future
    def __init__(self, short_name: str, ingredients: list, details: str):
        """
        Constructor -- creates new instance of recipe
        Parameters:
            self -- the current recipe
            ingredients -- a list of ingredients
            details -- how to cook the dish in details
        """
        self.__short_name = short_name
        self.__ingredients = ingredients.copy()  # To protect the list
        self.__details = details

    @property
    def short_name(self):
        """Returns the short name of the recipe"""
        return self.__short_name

    @property
    def ingredients(self):
        """Returns the ingredients of the recipe"""
        return self.__ingredients

    @property
    def details(self):
        """Returns the details of the recipe"""
        return self.__details

    @short_name.setter
    def short_name(self, new_short_name):
        """Sets new short name"""
        self.__short_name = new_short_name

    @ingredients.setter
    def ingredients(self, new_ingredients):
        """Sets new ingredients"""
        self.__ingredients = new_ingredients

    @details.setter
    def details(self, new_details):
        """Sets new details"""
        self.__details = new_details

    def check_ingredients(self, available_ingredients):
        """Checks the unavailable ingredients of a recipe"""
        unavailable_ingredients = []
        for ingredient in self.ingredients:
            if ingredient not in available_ingredients:
                unavailable_ingredients.append(ingredient)
        return unavailable_ingredients

    def __str__(self):
        """
        Method -- returns a string that represents this recipe
        Parameters:
            self -- the current recipe
        """
        name_output = self.short_name + ":\n"
        ingredients_output = "ingredients: \n"
        ingredients_output += str(self.ingredients).strip("[]") + "\n"
        details_output = "details: \n " + self.details
        output = name_output + ingredients_output + details_output
        return output


def load_recipes_from_file(filename: str) -> list:
    """
    Loads recipes from a file

    Parameters:
        filename(str)

    Returns:
        recipes(list)
    """
    recipes = []
    with open(filename, "r") as csvfile:
        recipes_reader = csv.reader(csvfile)
        for row in recipes_reader:
            short_name = row[0]
            ingredients = row[1].strip("[]").replace("'", "")
            ingredients = ingredients.split(",")
            ingredients = list(map(str.strip, ingredients))
            details = row[2]
            recipe = Recipe(short_name, ingredients, details)
            recipes.append(recipe)
        return recipes


def save_recipes_to_file(filename: str, recipes: list[Recipe]) -> None:
    """
    Saves recipes to a file

    Parameters:
        filename(str)
        recipes(list)

    Returns:
        None
    """
    with open(filename, "w", newline="") as csvfile:
        recipes_writer = csv.writer(csvfile)
        for recipe in recipes:
            row = [recipe.short_name, recipe.ingredients, recipe.details]
            recipes_writer.writerow(row)
