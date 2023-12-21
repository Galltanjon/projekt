class MenuItem():
    """Imports the menu from the text file 'menu.txt' and compares the user's input with existing options"""
    def __init__(self, name, ingredients, price):
        self.ingredients = ingredients
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}\nIngredients: {', '.join(self.ingredients)}\nPrice: {self.price} SEK"



def read_menu(file_path):
    """Reads menu text file 4 lines at a time and stores them as instances of Menu in menus list."""

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
    def __init__(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price

    def __str__(self): 
        return f"{self.ingredients}\nPrice: {self.price} SEK"
    

def read_options(file_path):
    """Reads addons text file 2 lines at a time and stores them as instances of addons in addons list."""  
    options = []
    with open(file_path, "r", encoding="utf-8") as f: 
        lines = f.read().splitlines()
    for i in range(0, len(lines), 2):
        ingredients = str(lines[i])
        price = int(lines[i + 1])
        option = Options(ingredients, price)
        options.append(option)
    return options


def user_wishes(bar, options):
    wishes = []
    ingredients = []
    print(f"Welcome to salad bar {bar}\nEnter the ingredients you want\nWrite done when finished\n>")  
    while ingredients != "done":
        ingredients = input("Ingredients: ").lower()
        if ingredients == "done":
            break
        elif ingredients not in [option.ingredients for option in options]: #chatGPT used for part after 'not in'
            print("This ingredient is not available")
        else:
            wishes.append(ingredients)       
    print(wishes) #to be removed
    return wishes



def find_best_match(user_wishes, menus):
    best_match = None
    max_matching_ingredients = 0

    for menu in menus:
        matching_ingredients = len(set(user_wishes).intersection(menu.ingredients)) #chatGPT used for matching function
        
        if matching_ingredients > max_matching_ingredients:
            max_matching_ingredients = matching_ingredients
            best_match = menu
        elif matching_ingredients == max_matching_ingredients and menu.price < best_match.price:
            best_match = menu

    if best_match:
        needed_ingredients = set(best_match.ingredients) - set(user_wishes)
        return best_match, needed_ingredients
    else:
        return None, None



def main():
    bar = input("Write 1 for the first salad bar or 2 for the second\n>")
    menus = read_menu(f"{bar}menu.txt")
    options = read_options(f"{bar}options.txt")

    for menu in menus:
        print(menu)
        print("------------------------")

    for option in options:
        print(option)
        print("------------------------")

    user_wishes_list = user_wishes(bar, options)

    best_match, needed_ingredients = find_best_match(user_wishes_list, menus)

    if best_match:
        print(f"\nBest Match: {best_match.name}\nPrice: {best_match.price} SEK")
        print("Needed Ingredients:")
        for ingredient in needed_ingredients:
            print(ingredient)
    else:
        print("No matching item found.")

if __name__ == "__main__":
    main()
