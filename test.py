class Items:
    """Imports single ingredients and dressings from text file 'addons.txt' to be handled as objects"""

    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item {self.number}: {self.name}\nPrice: {self.price} SEK"
    


#Läs in items






class Options():
    """Imports the menu from the text file 'menu.txt'."""

    def __init__(self, number, name, ingredients, price):

        self.number = number
        self.name = name
        self.ingredients = ingredients
        self.price = price


    def __str__(self):

        return f"Menu {self.number}: {self.name}\nIngredients: {', '.join(self.ingredients)}\nPrice: {self.price} SEK"
    







    def read_menu():

        menus = []
        menus_ingredients = {}
        menus_prices = {}

        with open("menu.txt", "r", encoding="utf-8") as f: #Här någonstans ska flera olika menyer kunna väljas
            lines = f.read().splitlines()

        for i in range(0, len(lines), 4):
            number = int(lines[i])
            name = lines[i + 1]
            ingredients = lines[i + 2].split(', ')
            ingredients.sort()
            price = int(lines[i + 3])

            menu_options = Options(number, name, ingredients, price)

            menus.append(menu_options)
            menus_ingredients.update({number : ingredients})
            menus_prices.update({number : price})

        return menus, menus_ingredients, menus_prices
    
menus, menus_ingredients, menus_prices = Options.read_menu()

#menus = read_menu()
for menu in menus:
    print(menu) #Just menu to read each instance, menu.ingredients for each ingredients list, menu.price for instants price etc.
    print("------------------------")

        
print(menus_ingredients)
