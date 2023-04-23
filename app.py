""" 
This is the main entry point for the application.

NAME: Jiahui Zhou
SEMESTER: 2023 Spring
"""
import string
import view
import recipe


FILE_NAME = "recipe.csv"


def format_short_name(short_name):
    """
    Formats the short name of the recipe
    Capitalizes first letters of each word of the short name
    """
    formatted_short_name = string.capwords(short_name)
    return formatted_short_name


def format_ingredients(ingredients):
    """Formats the ingredients into a list"""
    if "," in ingredients:
        ingredients_list = ingredients.split(",")
    else:
        ingredients_list = ingredients.split(" ")
    return ingredients_list


def handle_load(recipes) -> list:
    """Handles the load command"""
    try:
        recipes = recipe.load_recipes_from_file(FILE_NAME)
        view.print_hint("Load successfully!")
    except IndexError:  # in case of incomplete information
        view.print_error("Index Error!")
    except FileNotFoundError:  # in case of file not exists
        view.print_error("File not found!")
        view.print_hint("Please save recipes first!")
    return recipes


def handle_save(recipes: list) -> None:
    """Handles the save command"""
    try:
        recipe.save_recipes_to_file(FILE_NAME, recipes)
        view.print_hint("Save successfully!")
    except PermissionError:  # in case of file is opened
        view.print_error("Permission denied!")


def handle_add(recipes: list):
    """Handles the add command"""
    short_name = view.get_recipe_short_name()
    formatted_short_name = format_short_name(short_name)
    ingredients_input = view.get_recipe_ingredients()
    ingredients = format_ingredients(ingredients_input)
    details = view.get_recipe_details()
    new_recipe = recipe.Recipe(formatted_short_name, ingredients, details)
    recipes.append(new_recipe)
    return recipes


def handle_remove(recipes: list):
    """Handles the remove command"""
    short_name_of_recipe_to_remove = view.get_recipe_query()
    for rcp in recipes:  # use for loop to find the target recipe
        if short_name_of_recipe_to_remove in rcp.short_name.lower():
            if view.get_confirmation(rcp.short_name):
                recipes.remove(rcp)
                view.print_hint("Remove successfully!")
                return recipes
    view.print_hint("Cannot find the recipe!")
    return recipes


def handle_list(recipes: list):
    """Handles the list command"""
    if len(recipes) == 0:
        return view.print_hint("Empty list! please add or load recipes first")
    return view.print_recipes(recipes)


def handle_check(recipes: list) -> None:
    """Handles the check command"""
    short_name_of_recipe_to_check = view.get_recipe_query()
    for rcp in recipes:  # use for loop to find the target recipe
        if short_name_of_recipe_to_check in rcp.short_name.lower():
            if view.get_confirmation(rcp.short_name):
                available_input = view.get_available_ingredients()
                available_ingredients = format_ingredients(available_input)
                unavailable = rcp.check_ingredients(available_ingredients)
                if len(unavailable) != 0:
                    view.print_unavailable_ingredients(unavailable)

                else:
                    view.print_hint("All ingredients are available!")
                return None
    view.print_hint("Cannot find the recipe!")


def handle_unknown():
    """Handles unknown command"""
    view.print_hint("Please input a command above!")


def main():
    """This is the main entry point for application"""
    recipes = []
    view.print_welcome()
    view.print_menu()
    command = view.get_command()
    while command != view.ViewOptions.EXIT:
        if command == view.ViewOptions.LIST:
            handle_list(recipes)
        elif command == view.ViewOptions.ADD:
            recipes = handle_add(recipes)
        elif command == view.ViewOptions.REMOVE:
            recipes = handle_remove(recipes)
        elif command == view.ViewOptions.CHECK:
            handle_check(recipes)
        elif command == view.ViewOptions.SAVE:
            handle_save(recipes)
        elif command == view.ViewOptions.LOAD:
            recipes = handle_load(recipes)
        elif command == view.ViewOptions.UNKNOWN:
            handle_unknown()
        command = view.get_command()


if __name__ == "__main__":
    main()
