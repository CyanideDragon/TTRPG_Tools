from scripting.action import Action
import random
"Working on a way to create a dictionary of lists. I am not certain how to return what they have gotten "
class RollTable(Action):
    def __init__(self):
        pass
    Tavern = ["1: A group of bandits attack the tavern", "2 The bartender offers free drinks in exchange for killing some rodents running around the place", "3: The barkeep has information related to the parties quest, or a particular player's story", "4: A pair of grizzled veterens are harrasing the barmaids", "5: A noble staying there has bought out all the rooms, and stable stalls at the tavern despite him only having two bodyguards with him. He seems to have a strong dislike of the party", "6: An traveling magician performing at the tavern, has a spell go terribly awry. Roll on the Wild magic table."]
    Weather = ["1: ", "2: ", "3: ", "4: ", "5: ", "6"]
    boat_travel = ["1: ", "2: ", "3: ", "4: ", "5: ", "6"]
    horse_travel = ["1: ", "2: ", "3: ", "4: ", "5: ", "6"]
    severe_weather = ["1: ", "2: ", "3: ", "4: ", "5: ", "6"]
    monster_attack = ["1: ", "2: ", "3: ", "4: ", "5: ", "6"]
    current_roll_tables= {[0, {Tavern}], [1, {Weather}], [2, {boat_travel}] , [3, {horse_travel}], [4, {severe_weather}], [5, {monster_attack}]}
    print(f"{current_roll_tables}")
    user_input = input("What kind of roll table do you want 1-10")
    selected_table = current_roll_tables[user_input]
    dice_roll = random.randint(1, 6)
    output = selected_table[dice_roll]
    def execute(self, dice_type):
        dice_roll = random.randint(1, dice_type)
        return super().execute()