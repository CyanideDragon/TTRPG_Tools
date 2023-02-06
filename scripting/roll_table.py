from scripting.action import Action
import random
from scripting.dice_roll_action import DiceRollAction
"Working on a way to create a dictionary of lists. I am not certain how to return what they have gotten "
class RollTable(Action):
    def __init__(self):
        self.tavern = {1: "A group of bandits attack the tavern", 2: "The bartender offers free drinks in exchange for killing some rodents running around the place", 3: "The barkeep has information related to the parties quest, or a particular player's story", 4: "A pair of grizzled veterens are harrasing the barmaids", 5: "A noble staying there has bought out all the rooms, and stable stalls at the tavern despite him only having two bodyguards with him. He seems to have a strong dislike of the party", 6: "An traveling magician performing at the tavern, has a spell go terribly awry. Roll on the Wild magic table."}
        self.weather = {1: "test" , 2: "test", 3: "test", 4: "test", 5 :"test", 6: "test"}
        self.boat_travel = {1: "test" , 2: "test", 3: "test", 4: "test", 5 :"test", 6: "test"}
        self.horse_travel = {1: "test" , 2: "test", 3: "test", 4: "test", 5 :"test", 6: "test"}
        self.severe_weather = {1: "test" , 2: "test", 3: "test", 4: "test", 5 :"test", 6: "test"}
        self.monster_attack = {1: "test" , 2: "test", 3: "test", 4: "test", 5 :"test", 6: "test"}
        self.current_roll_tables= {"tavern" : self.tavern ,"weather" : self.weather,"boat travel" : self.boat_travel,"horse travel": self.horse_travel,"severe weather": self.severe_weather,"monster attack": self.monster_attack}
    # print(f"{current_roll_tables}")
    # user_input = input("What kind of roll table do you want 1-10")
    # selected_table = current_roll_tables[user_input]

    def execute(self, user_input):
        dice_roll = DiceRollAction.execute(self.current_roll_tables[user_input].size() )
#Might need to indicate a +1 for safety reasons
        self.current_roll_tables[user_input[dice_roll[2]]]
        return super().execute()
