from scripting.action import Action
import random
from scripting.dice_roll_action import DiceRollAction
"Working on a way to create a dictionary of lists. I am not certain how to return what they have gotten "
class Events(Action):
    def __init__(self):
        self.event = {1: "test", 2: "test", 3: "test", 4: "test", 5: "test", 6: "test", 7: "test", 8: "test", 9: "test", 10: "test", 11: "test", 12: "test", 13: "test", 14: "test", 15: "test", 16: "test", 17: "test", 18: "test", 19: "test", 20: "test",}
    # print(f"{current_roll_tables}")
    # user_input = input("What kind of roll table do you want 1-10")
    # selected_table = current_roll_tables[user_input]

    def execute(self, user_input):
        dice_roll = DiceRollAction.execute(self.current_roll_tables[user_input].size() )
#Might need to indicate a +1 for safety reasons
        self.current_roll_tables[user_input[dice_roll[2]]]
        return super().execute()