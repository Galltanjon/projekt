class Menu():
    """Imports the menu from the text file 'menu.txt' and compares the user's input with existing options"""

    def __init__(self, number, name, ingredients, price):
        self.ingredients = ingredients
        self.number = number
        self.name = name
        self.price = price

    def __str__(self):
        """Corrected by ChatGPT"""
        return f"Menu {self.number}: {self.name}\nIngredients: {', '.join(self.ingredients)}\nPrice: {self.price} SEK"

def read_menu():
    """Reads menu text file 4 lines at a time and stores them as instances of Menu in menus list.
    
    Creates empty list, then opens and reads the entire text file, splitting and storing every line as an element in a list.
    (0, len(lines), 4) means that the loop starts with first line, ends with last line - previously defined as the last element of the file.
    The 4 means that after the loop processes i=0, i=0+1, up to i=0+4, i changes value to 4 and starts again (i=4, i=4+1...
    since that's how the text file list is structured. Each loop is then stored as an instance of the Menu class within the menus list.
    When calling upon the list a loop is used to include the string representation of the Menu instances (!=__main__.Menu object at 0x00000)"""

    menus = []

    with open("menu.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i in range(0, len(lines), 4):
        number = int(lines[i])
        name = lines[i + 1]
        ingredients = lines[i + 2].split(', ') #specific split usage found via chatGPT
        price = int(lines[i + 3])

        menu = Menu(number, name, ingredients, price)
        menus.append(menu)

    return menus

menus = read_menu()
for menu in menus:
    print(menu.ingredients) #Just menu to read each instance, menu.ingredients for each ingredients list, menu.price for instants price etc.
    print("------------------------")

class AddOn
