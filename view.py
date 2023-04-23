""" 
This is the main view for the application. It is responsible for
displaying the information to the client, and getting input from the client.

NAME: Jiahui Zhou
SEMESTER: 2023 Spring
"""
import sys
from enum import Enum

import recipe


class ViewOptions(Enum):
    """ The options for the view """
    EXIT = 1
    LIST = 2
    ADD = 3
    REMOVE = 4
    CHECK = 5
    SAVE = 6
    LOAD = 7
    UNKNOWN = 8


def print_welcome() -> None:
    """ Prints the welcome message """
    print("Welcome to the dinning advice app")
    print("Type 'help' to get a list of commands.")


def print_goodbye() -> None:
    """ Prints the goodbye message """
    print("Goodbye, bon appetit!")


def print_error(message: str) -> None:
    """
    Prints an error message

    Args:
        message (str): error message to print
    """
    print(f'Error: {message}', file=sys.stderr)


def print_hint(message: str) -> None:
    """Prints a hint message"""
    print(f'Hint: {message}')


def print_recipe(rcp: recipe.Recipe):
    """Prints a recipe"""
    print(rcp)


def print_menu() -> None:
    """Prints the menu"""
    print("Type any of the following commands. You can also type the number.")
    print("1. Exit - save the modifications and exit the program")
    print("2. List - list the existing recipes")
    print("3. Add - add a recipe")
    print("4. Remove - remove a recipe")
    print("5. Check - check ingredients that you don't have")
    print("6. Save - remove the recipes to a file")
    print("7. Load - load recipes from a file")


def get_recipe_query():
    """
    Gets the recipe to query for

    Returns:
        Recipe
    """
    return input("Enter the short name of the recipe").strip().lower()


def get_confirmation(short_name):
    """ Asks for confirmation"""
    confirmation = input(f"Is it {short_name}? Type 'y' for yes or 'n' for no").strip().lower()
    return confirmation == "y" or confirmation == "yes"


def get_recipe_short_name():
    """Gets the short name of the recipe"""
    return input("What's the name of this recipe?").strip().lower()


def get_recipe_ingredients():
    """
    Gets ingredients of this recipe,
    assuming that the ingredients are separated with comma or whitespace
    """
    text = "What are the ingredients of this recipe?\n"
    text += "Please separate them with comma or whitespace\n"
    ingredients = input(text).strip().lower()
    return ingredients


def get_recipe_details():
    """Gets the details of the recipe"""
    return input("How to cook this dish?").strip().lower()


def get_available_ingredients():
    """
    Gets the available_ingredients
    assuming that the ingredients are separated with comma or whitespace
    """
    text = "What ingredients do you have?\n"
    text += "Please separate them with comma or whitespace\n"
    ingredients = input(text).strip().lower()
    return ingredients


def print_unavailable_ingredients(unavailable_ingredients: list):
    """Prints unavailable ingredients"""
    result = "Unavailable ingredients: "
    for ingredient in unavailable_ingredients:
        result += ingredient
        result += " "
    print(result)


def print_recipes(recipes: list):
    """Prints a list of recipes"""
    for rcp in recipes:
        print("-" * 10)
        print(rcp)
    print("-" * 10)


def get_command() -> ViewOptions:
    """Gets the command from the user"""
    command = input("What do you like to do?").lower()
    if command == "exit" or command == "1":
        return ViewOptions.EXIT
    elif command == "list" or command == "2":
        return ViewOptions.LIST
    elif command == "add" or command == "3":
        return ViewOptions.ADD
    elif command == "remove" or command == "4":
        return ViewOptions.REMOVE
    elif command == "check" or command == "5":
        return ViewOptions.CHECK
    elif command == "save" or command == "6":
        return ViewOptions.SAVE
    elif command == "load" or command == "7":
        return ViewOptions.LOAD
    else:
        return ViewOptions.UNKNOWN
