from scripting.action import Action
from scripting.dice_roll_action import DiceRollAction
import constants

class DoWeaponItemAction:
    def __init__(self):
        self.item_modifiers = constants.ITEM_MODIFIER_CODES

    def execute(self, item_name, item_modifiers, item_range, item_damage, player_modifier, item_magic = None):
        #default means that not all items have these modifiers

        item_damage = item_damage.split('d')
        number_of_dice = int(item_damage[0])
        die_size = int(item_damage[1])
        damage_result = 0

        for x in range(item_modifiers.split(" ")):
            if item_modifiers == self.item_modifiers["two-handed"]:
                die_size += 2
                """two-handed swings makes attacks stronger."""

            #add more if statements for other weapon mods that change damage or die sizes

        for _ in number_of_dice:
            roller_return = DiceRollAction.execute(die_size)
            damage_result += roller_return[2]
        
        damage_result += player_modifier

        print(damage_result)
        


        pass