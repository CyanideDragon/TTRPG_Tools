from scripting.action import Action

class CreateInventoryItems:
    #Class should only be called by one other function that stores the items into memory.

    def __init__(self):
        pass

    def execute(self):
        with open("inventory_items.txt", "r") as item_file:
            item_dict = {}
            next(item_file)
            for line in item_file:
                line = line.strip().split(", ")
                #Tried to do dictionary comprehension for less coding but it made the snake angry.
                key, value = line[0], line[1:]
                #Keys will always be item names. names will be stored in all lower case and with normal typed formatting. any numbers will need to be converted into ints/float
                #Dictionary only wants to store items as strings with this setup. Make sure to code int and float requests. It would be more effort turning into ints and floats here.
                item_dict[key] = value
        return item_dict