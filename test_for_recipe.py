"""
This is the test file for recipe, including all methods,
save to file and load from file functions.
NAME: Jiahui Zhou
SEMESTER: 2023 Spring
"""
import unittest

from recipe import Recipe
from recipe import load_recipes_from_file, save_recipes_to_file


class TestItem(unittest.TestCase):
    def test_str_1(self):
        """Tests a string of recipe with one ingredient"""
        rcp = Recipe("Toasted Chicken", ["chicken"], "Toast it.")
        self.assertEqual(str(rcp),
                         "Toasted Chicken:\ningredients: \n\'chicken\'\ndetails: \n Toast it.")


    def test_str_2(self):
        """Tests a string of recipe with empty input"""
        rcp = Recipe("", [""], "")
        self.assertEqual(str(rcp), ":\ningredients: \n''\ndetails: \n ")


    def test_check_ingredients1(self):
        """Tests with all ingredients available"""
        rep = Recipe("Toasted Chicken", ["chicken"], "Toast it.")
        self.assertEqual(rep.check_ingredients(["chicken"]), [])


    def test_check_ingredients2(self):
        """Tests with unneeded ingredients"""
        rep = Recipe("Toasted Chicken", ["chicken"], "Toast it.")
        self.assertEqual(rep.check_ingredients(["pork"]), ["chicken"])


    def test_load_recipes_from_file1(self):
        """Tests loading recipes from a csv file"""
        rcps = load_recipes_from_file("expected file 1.csv")
        output = ""
        for rcp in rcps:
            output += str(rcp)
        expected = "Salad:\ningredients: \n'vegetable', 'fruit', " \
                    "'cheese'\ndetails: \n Mingle them.Toasted " \
                    "Chicken:\ningredients: \n'chicken'\n" \
                    "details: \n Toast it."
        self.assertEqual(output, expected)


    def test_load_recipes_from_file2(self):
        """Tests loading recipes from a csv file"""
        rcps = load_recipes_from_file("expected file 2.csv")
        output = ""
        for rcp in rcps:
            output += str(rcp)
        expected = "French Fries:\ningredients: \n'potato'\ndetails: \n " \
                   "Fry it."
        self.assertEqual(output, expected)


    def test_save_recipes_to_file1(self):
        """Tests saving a list of recipes to a csv file"""
        a = Recipe("Salad",["vegetable","fruit","cheese"], "Mingle them.")
        b = Recipe("Toasted Chicken", ["chicken"], "Toast it.")
        save_recipes_to_file("test1.csv", [a, b])
        with open("expected file 1.csv") as file1, open("test1.csv") as file2:
            contents_one = file1.read()
            contents_two = file2.read()
        self.assertEqual(contents_one,contents_two)


    def test_save_recipes_to_file2(self):
        """Tests saving a list of recipes to a csv file"""
        a = Recipe("French Fries", ["potato"], "Fry it.")
        save_recipes_to_file("test2.csv", [a])
        with open("expected file 2.csv") as file1, open("test2.csv") as file2:
            contents_one = file1.read()
            contents_two = file2.read()
        self.assertEqual(contents_one,contents_two)
