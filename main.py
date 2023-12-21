import sys
class MenuItem():
    """Defines class MenuItem representing an item or alternative on the menu"""

    def __init__(self, name, ingredients, price):
        """Initialises instance of MenuItem"""

        self.ingredients = ingredients
        self.name = name
        self.price = price

    def __str__(self):
        """Returns a string representation of the MenuItem"""

        return f"{self.name}\nIngredients: {', '.join(self.ingredients)}\nPrice: {self.price} SEK"


def read_menu(file_path):
    """Reads menu text file 3 lines at a time and stores them as instances of MenuItem in menus list."""

    menus = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines), 3):
        name = lines[i]
        ingredients = lines[i + 1].split(', ')
        ingredients.sort()
        price = int(lines[i + 2])
        menu = MenuItem(name, ingredients, price)
        menus.append(menu)
    return menus


class Options():
    """Defines class Options representing additional options (single items) or addons"""

    def __init__(self, ingredients, price):
        """Initialises instance of Options"""

        self.ingredients = ingredients
        self.price = price

    def __str__(self): 
        """Returns a string representation of the MenuItem"""

        return f"{self.ingredients}\nPrice: {self.price} SEK"


def read_options(file_path):
    """Reads options text file 2 lines at a time and stores them as instances of addons in addons list."""  
    options = []
    with open(file_path, "r", encoding="utf-8") as f: 
        lines = f.read().splitlines()
    for i in range(0, len(lines), 2):
        ingredients = str(lines[i])
        price = int(lines[i + 1])
        option = Options(ingredients, price)
        options.append(option)
    return options


def user_wishes(options):
    """Lets user enter desired ingredients until they enter 'done'.
    Checks if entered ingredient is actually an option."""

    wishes = []
    ingredients = []
    print("Enter the ingredients you want separated by [enter]\nWrite done when finished")  
    while ingredients != "done":
        ingredients = input("Ingredients: ").lower()
        if ingredients == "done":
            break
        elif ingredients not in [option.ingredients for option in options]: #chatGPT - Checks if user-entered ingredients are in list of ingredients found in any options instance
            print("This ingredient is not available")
        else:
            wishes.append(ingredients)       
    return wishes


def find_best_match(user_wishes, menus, options):
    """Finds best menu match based on user input.
    Also finds ingredients to be completed"""

    best_match = None
    max_matching_ingredients = 0
    extra_ingredients = {}

    for menu in menus:
        matching_ingredients = len(set(user_wishes).intersection(menu.ingredients))

        if matching_ingredients > max_matching_ingredients:
            max_matching_ingredients = matching_ingredients
            best_match = menu
            extra_ingredients = {ingredient: next((option.price for option in options if option.ingredients == ingredient), 0) for ingredient in set(user_wishes) - set(best_match.ingredients)}
        elif matching_ingredients == max_matching_ingredients and (best_match is None or menu.price < best_match.price):
            best_match = menu
            extra_ingredients = {ingredient: next((option.price for option in options if option.ingredients == ingredient), 0) for ingredient in set(user_wishes) - set(best_match.ingredients)}

    if best_match:
        needed_ingredients = set(best_match.ingredients) - set(user_wishes)
        return best_match, needed_ingredients, extra_ingredients
    else:
        closest_match = min(menus, key=lambda x: len(set(user_wishes).intersection(x.ingredients)))
        missing_ingredients = set(closest_match.ingredients) - set(user_wishes)

        # Initialize extra ingredients with their costs based on available options
        extra_ingredients = {ingredient: next((option.price for option in options if option.ingredients == ingredient), None) for ingredient in set(user_wishes) - set(closest_match.ingredients)}

        return closest_match, missing_ingredients, extra_ingredients



def addons(options, user_wishes_list, order_cost):
    """Lets user enter desired addons/single items/ingredients until they enter 'done'.
    Checks if entered ingredient is actually an option."""

    addons_wishes = []
    print("Enter the addons you want separated by [enter]\nWrite done when finished")
    while True:
        ingredient = input("Addon: ").lower()
        if ingredient == "done":
            break
        
        matching_option = next((option for option in options if option.ingredients == ingredient), None) #chatGPT - Checks if user-entered ingredients are in list of ingredients found in any options instance
        if matching_option:
            order_cost += matching_option.price
            addons_wishes.append((ingredient, matching_option.price))
            print(f"Added {ingredient} to your order. Additional cost: {matching_option.price} SEK")
        else:
            print(f"Addon {ingredient} not found in options.")
    return order_cost, addons_wishes


def choose_bar():
    """Choose between (in this case) bar 1 or 2"""
    while True:
            bar = input("Write '1' for the first salad bar or '2' for the second\n>")
            if bar == "1" or bar == "2":
                break
            else:
                print("Choose either 1 or 2")

    print(f"Welcome to salad bar {bar}")
    menus = read_menu(f"{bar}menu.txt")
    options = read_options(f"{bar}options.txt")

    for option in options:
        print(option)
        print("------------------------")
    
    return menus, options

def find_extra_ingredient_cost(extra_ingredients, options):
    """Finds the cost of extra ingredients based on available options."""
    extra_ingredient_cost = 0
    for extra_ingredient in extra_ingredients:
        matching_option = next((option for option in options if option.ingredients == extra_ingredient), None)
        if matching_option:
            extra_ingredient_cost += matching_option.price
    return extra_ingredient_cost

def receipt(best_match, addons_wishes, extra_ingredients, total_order_cost):
    """Writes receipt including ordered items and their costs, as well as total cost."""
    with open("receipt.txt", "w") as receipt_file:
        receipt_file.write(f"{best_match.name}: {best_match.price} SEK\n")

        for addon, addon_price in addons_wishes:
            receipt_file.write(f"{addon}: {addon_price} SEK\n")

        if extra_ingredients:
            receipt_file.write("\nExtra Ingredients:\n")
            for ingredient, extra_ingredient_cost in extra_ingredients.items():
                receipt_file.write(f"{ingredient}: {extra_ingredient_cost} SEK\n")

            # Calculate the total cost of extra ingredients
            extra_ingredients_cost = sum(extra_ingredients.values())
            receipt_file.write(f"Additional cost for extra ingredients: {extra_ingredients_cost} SEK\n")

        receipt_file.write(f"Total cost: {total_order_cost} SEK")

def main(menus, options):
    """Takes user input to select a salad bar.
    Reads menu and options from the selected bar.
    Takes user input for the main order and addons.
    Displays the best match for the main order and needed ingredients.
    Provides options to complete the order, add addons, or start a new order.
    Prints a receipt based on the completed order."""

    total_order_cost = 0

    while True:
        order_cost = 0
        addons_wishes = []  
        extra_ingredients = set()

        user_wishes_list = user_wishes(options)
        best_match, needed_ingredients, extra_ingredients = find_best_match(user_wishes_list, menus, options)

        if best_match:
            print(f"\nBest Match: {best_match.name}\nPrice: {best_match.price} SEK")
            if needed_ingredients:
                print("Needed Ingredients:")
                for ingredient in needed_ingredients:
                    print(ingredient)
            if extra_ingredients:
                print("\nExtra Ingredients:")
                for ingredient in extra_ingredients:
                    print(ingredient)
                # Calculate the cost of extra ingredients
                extra_ingredient_cost = find_extra_ingredient_cost(extra_ingredients, options)
                print(f"Additional cost for extra ingredients: {extra_ingredient_cost} SEK")
                order_cost += extra_ingredient_cost

            while True:
                accept_order = input("'yes' to complete the main order, 'no' to add addons, 'q' to quit\n>")
                if accept_order == "yes":
                    order_cost += best_match.price
                    total_order_cost += order_cost
                    break  # Exit the loop after successfully processing the order
                elif accept_order == "no":
                    order_cost, addons_wishes = addons(options, user_wishes_list, order_cost)
                    order_cost += best_match.price
                    total_order_cost += order_cost
                    break  # Exit the loop after successfully processing the order
                elif accept_order == "q":
                    sys.exit()
                else:
                    print("Write 'yes', 'no' or 'new'")
        else:
            print("No suggestion found. Try a new order")

        receipt(best_match, addons_wishes, extra_ingredients, order_cost)

        print("Here is the receipt")
        print("Enjoy!")
        break

if __name__ == "__main__":
    menus, options = choose_bar()
    main(menus, options)
