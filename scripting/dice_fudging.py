from scripting.action import Action
import random
from scripting.dice_roll_action import DiceRollAction
class DiceFudging(Action):
    def __init__(self):
        pass
    # user_input = input("What kind of roll table do you want 1-10")
    # selected_table = current_roll_tables[user_input]

    def execute(self, user_input):
        dice_roll = DiceRollAction.execute(self.current_roll_tables[user_input].size() )
#Might need to indicate a +1 for safety reasons
        self.current_roll_tables[user_input[dice_roll[2]]]
        return super().execute()