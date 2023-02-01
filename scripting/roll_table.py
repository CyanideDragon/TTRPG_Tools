from scripting.action import Action
import random

class RollTable(Action):
    def __init__(self):
        pass
    current_roll_tables= {[0, "Tavern"], [1, "Weather"], [2, "Boat travel"] , [3, "Travel on horseback"], [4, "Severe weather"], [5, "Monster attack"]}
    print(f"{current_roll_tables}")
    user_input = input("What kind of roll table do you want 1-10")
    selected_table = current_roll_tables[user_input]
    def execute(self, dice_type):
        dice_roll = random.randint(1, dice_type)
        return super().execute()