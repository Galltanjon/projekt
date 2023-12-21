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
    print("Enter the ingredients you want\nWrite done when finished")  
    while ingredients != "done":
        ingredients = input("Ingredients: ").lower()
        if ingredients == "done":
            break
        elif ingredients not in [option.ingredients for option in options]: #chatGPT - Checks if user-entered ingredients are in list of ingredients found in any options instance
            print("This ingredient is not available")
        else:
            wishes.append(ingredients)       
    return wishes


def find_best_match(user_wishes, menus):
    """Finds best menu match based on user input.
    Also finds ingredients to be completed"""

    
    
    best_match = None
    max_matching_ingredients = 0

    for menu in menus:
        matching_ingredients = len(set(user_wishes).intersection(menu.ingredients)) #chatGPT - calculated count of matching ingredients between users wishes and current menu

        if matching_ingredients > max_matching_ingredients: #With every loop through menus this checks if (from top to bottom) the row it is on is a better match or not, updates best current match if it is
            max_matching_ingredients = matching_ingredients
            best_match = menu
        elif matching_ingredients == max_matching_ingredients and (best_match is None or menu.price < best_match.price):
            best_match = menu

    if best_match:  #If any good match, the difference between user input and best match will be what has to be completed
        needed_ingredients = set(best_match.ingredients) - set(user_wishes)
        return best_match, needed_ingredients
    else:
        #Gives set of common elements and the length of commonality for every menu, highest number wins the comparison and is thereby closest match
        closest_match = min(menus, key=lambda x: len(set(user_wishes).intersection(x.ingredients))) #chatGPT for this row
        missing_ingredients = set(closest_match.ingredients) - set(user_wishes)
        return closest_match, missing_ingredients


def addons(options, user_wishes_list, order_cost):
    """Lets user enter desired addons/single items/ingredients until they enter 'done'.
    Checks if entered ingredient is actually an option."""

    addons_wishes = []
    print("Enter the addons you want\nWrite done when finished")
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


def receipt(best_match, addons_wishes, order_cost):
    """Writes receipt including ordered items and their costs, as well as total cost."""

    with open("receipt.txt", "w") as receipt:
        receipt.write(f"{best_match.name}: {best_match.price} SEK\n")
        for addon, addon_price in addons_wishes:
            receipt.write(f"{addon}: {addon_price} SEK\n")
        receipt.write(f"Total cost: {order_cost} SEK")
    return receipt


def main():
    """Takes user input to select a salad bar.
    Reads menu and options from selected bar.
    Takes user input for main order and addons.
    Displays the best match for the main order and needed ingredients.
    Provides options to complete the order, add addons, or start a new order.
    Prints receipt based on the completed order."""

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

    order_cost = 0
    addons_wishes = [] 
    i = 0
    while i == 0:
        user_wishes_list = user_wishes(options)
        best_match, needed_ingredients = find_best_match(user_wishes_list, menus)

        if best_match:
            print(f"\nBest Match: {best_match.name}\nPrice: {best_match.price} SEK")
            if needed_ingredients:
                print("Needed Ingredients:")
                for ingredient in needed_ingredients:
                    print(ingredient)
                j = 0
                while j == 0:
                    accept_order = input("'yes' to complete main order, 'no' to add addons, 'new' to restart order\n>")
                    if accept_order == "yes":
                        order_cost += best_match.price
                        i = 1
                        j = 1
                    elif accept_order == "no":
                        order_cost, addons_wishes = addons(options, user_wishes_list, order_cost)  
                        order_cost += best_match.price
                        i = 1
                        j = 1
                    elif accept_order == "new":
                        i = 0
                        j = 1
                    else:
                        print("Write 'yes', 'no' or 'new'")
        else:
            print("No suggestion found. Try a new order")
            i = 0

    receipt(best_match, addons_wishes, order_cost)
    print("Here is the receipt")
    print("Enjoy!")

if __name__ == "__main__":
    main()
