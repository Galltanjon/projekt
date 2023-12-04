
class Ingredient:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Dressing:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost



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
            #quit

        else:
            user_ingredients.append(user_choice)
            print(user_ingredients)






        
user_freetext()

class Menu:
    def __init__(self, number, name, ingredients, dressing, price):
        self.number = number
        self.name = name
        self.ingredients = ingredients
        self.dressing = dressing
        self.price = price

        # Example usage
        menu_items = []
        with open("menu.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Parse the line and create Menu instances
                # ...
                cleaned_line = line.strip()
                print(cleaned_line)
                # Append Menu instance to the list
                menu_items.append(Menu(number, name, ingredients, dressing, price))

        print(menu_items)
    __init__()

class Order:
    def __init__(self):
        self.ingredients = []
        self.dressing = None
        self.modifications = []
        self.price = 0

    def __str__(self):
        """Returns a string representation of the salad"""

        return f"{self.ingredients} {self.modifications} {self.dressing} {self.price}"

    def calculate_cost(self):
        for ingredient in self.ingredients:
            self.price += ingredient.cost

        if self.dressing:
            self.price += self.dressing.cost

        # Add cost calculation for modifications
        # ...

def suggest_salad(user_ingredients, menu_items):
    # Implement logic to find matches or suggestions
    # ...

    # Return the best match or suggestions
    # ...
    return suggest_salad

def user_interaction():
    order = Order()

    while True:
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            print("Finding matches...")
            suggest_salad(order.ingredients, menu_items)
            order.calculate_cost()
            print(f"Total cost: {order.price}")

        elif user_choice == "2":
            order.remove_latest_ingredient()
            order.calculate_cost()

        elif user_choice == "3":
            break

        else:
            order.add_ingredient(user_choice)
            print(order)

user_interaction()

