class Salad:
    def __init__(self, menu_number, menu_name, ingredients, price):
        self.menu_number = menu_number
        self.menu_name = menu_name
        self.ingredients = ingredients
        self.price = price

    """def __str__(self):
        
        Returns a string representation of the salad
        #return f"{self.menu_number} {self.menu_name} {self.ingredients} {self.price}"
        #return str(self.menu_number) + " " + str(self.menu_name) + " " + str(self.ingredients) + " " + (str(self.price))"""

def read_menu():
    """Opens textfile of menus (UTF-8) and reads lines in groups of four (how each salad is structured in meny.txt), ending when no more lines.
    After each salad is read from file, an instance of the Salad class is created and each salad is stored in a dictionary with its menu number as key.
    Finally the user can see the menu (might be reworked to be read from the dictionary in its own function instead), and at last the textfile is closed."""

    menu_dict = {}
    # Open the text file for reading with UTF-8 encoding
    with open(r'C:\Users\flprk\Desktop\Workstation\Salladsprojekt\meny.txt', 'r', encoding='utf-8') as file:
        # Loop through the file and read 4 lines at a time
        while True:
            # Read 4 lines
            menu_number = file.readline().strip()
            menu_name = file.readline().strip()
            ingredients = file.readline().strip()
            price = file.readline().strip()

            # If any line is empty, break the loop. Hittat och utforskat via CHATGPT
            if not all([menu_number, menu_name, ingredients, price]):
                break

            # Create an instance of the Sallad class
            sallad_instance = Salad(menu_number, menu_name, ingredients, price)
            menu_dict[menu_number] = sallad_instance
            
            # Do something with the created instance (e.g., print its details)
            print("Menu Number:", sallad_instance.menu_number)
            print("Name:", sallad_instance.menu_name)
            print("Ingredients:", sallad_instance.ingredients)
            print("Price:", sallad_instance.price)
            print("----")  # Separation line between sets of 4 lines
    return menu_dict

# Call the read_menu function to read from the file and print the menu details
menu_items_dict = read_menu()

"""# Access individual menu items in the dictionary using menu numbers as keys
for menu_number, menu_item in menu_items_dict.items():
    print(f"Menu Number: {menu_number}")
    print(menu_item)
    print("----")  # Separation line between menu items"""
