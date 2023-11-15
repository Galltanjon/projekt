# Written by Filip Eriksson
# Group 38
#
# Description: The program should handle a vegetarian customer order
# and match the customer's preferences with the most suitable menu option.
# Then, the customer will navigate to the menu with additional choices before
# being able to pay and receive a receipt. The cost of ingredients is on a separate file.
#
#
#
#
#
#
#
#
# Everything will be translated to English

class Order():
    """Handles user input as an object"""

    def __init__(self, ingredients, modifications, dressing, price):
        """Defines the attributes of the salad"""

        self.ingredients = ingredients
        self.modifications = modifications
        self.dressing = dressing
        self.price = price

    def __str__(self):
        """Returns a string representation of the salad"""

        return f"{self.ingredients} {self.modifications} {self.dressing} {self.price}"

def user_freetext():
    """Allows the user to freely write what they want in their salad (modifications included here)"""

class Menu():
    """Imports the menu from the text file 'menu.txt' and compares the user's input with existing options"""

    def __init__(self, number, name, ingredients, price):
        self.ingredients = ingredients
        self.number = number
        self.name = name
        self.price = price

def read_menu():
    # A dictionary can store lists, which probably helps when storing all ingredients in a menu option behind a single digit (menu option)

    menu = {}
    with open(r"C:\Users\flprk\Desktop\Workstation\Salladsprojekt\menu.txt", "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            print(cleaned_line)

    return menu
read_menu()

    """def read_menu(): 
        Reads the menu from a text file
        file = open("menu.txt", "r", encoding="utf-8")
        menu_choice = file.readline().strip()
        while menu_choice:
        lastname = str(file.readline().strip())
        surname = str(file.readline().strip())
        new_student = Student(surname, lastname, personalnumber)
        self.students.append(new_student)
        personalnumber = file.readline().strip()
        file.close()"""

    def display_menu():
        """Presents the menu options to the user"""

    def match_salad():
        """Examines which menu options match the user's preferences and stores them in a list"""

    def suggest_salad():
        """If nothing matches directly, there is a function to suggest the closest matching option"""

class AddOn():
    """Imports add-ons from the text file 'addons.txt' and allows the user to choose a dressing or add ingredients"""

    def read_ingredients():
        """Reads ingredients and additions from another text file"""

    def display_addons():
        """After choosing everything else, the addons that can be added are presented"""

    def choose_addons():
        """Adds the addons with their costs if the user wants addons"""

def choose_option():
    """Allows the user to choose one of the options on the menu or the free text option"""

def modifications():
    """Allows the user to choose whether they want to add or remove ingredients in their salad"""

def calculate_total_cost():
    """Calculates the total cost based on menu choices and/or individual ingredient costs as well as addon costs"""

def pay_receipt():
    """The user is given the choice to pay, upon which they receive a receipt, or start over with the order"""

def main():
    """Organizes the remaining functions in a logical sequence"""
