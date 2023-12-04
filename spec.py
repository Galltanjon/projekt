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
#
class Menu():
    """Imports the menu from the text file 'menu.txt' and compares the user's input with existing options"""

    def __init__(self, number, name, ingredients, price):
        self.ingredients = ingredients
        self.number = number
        self.name = name
        self.price = price

    def __str__(self):
        return f"Menu {self.number}: {self.name}\nIngredients: {', '.join(self.ingredients)}\nPrice: {self.price} SEK"
    
    #menu_instance = Menu(1, 'wow salad', ['tofu', 'mixed greens', 'bulgur', 'tomato', 'cucumber'], 139)
    #print(menu_instance)

def read_menu():
    # A dictionary can store lists, which probably helps when storing all ingredients in a menu option behind a single digit (menu option)

    menu = {}
    with open("menu.txt", "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            print(cleaned_line)

    return menu
read_menu()

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
    user_ingredients = []
    i = 0
    print("What would you like to have in your salad?\nSeparate your input with enter")
    print("When you're satisfied with your input:\n>Press 1 to find matching alternatives\nOtherwise:\n>Press 2 to remove latest ingredient\n>Press 3 to quit\n")
    while i == 0:
        user_choice = (input(">"))
        if user_choice == "1":
            i += 1
            print("salad matching...")
            print("salad suggesting...")

        elif user_choice == "2": 
            try:
                print("Removed " + user_ingredients[-1])
                user_ingredients.pop()
            except IndexError:
                print("There are no ingredients to remove")

        elif user_choice == "3":
            i += 1
            quit

        else:
            user_ingredients.append(user_choice)
            print(user_ingredients)






        
user_freetext()






def display_menu():
        """Presents the menu options to the user"""

def match_salad():
    """Examines which menu options match the user's preferences and stores them in a list"""
    print("matching salad...")
    return match_salad()

def suggest_salad():
    """If nothing matches directly, there is a function to suggest the closest matching option"""
    print("suggesting salad...")
    return suggest_salad()

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
    #Welcome, choose ingredients
    #Now match or suggest salad, keep track of cost
    #Choose addons and dressing, keep track of cost
    #Calculate cost
