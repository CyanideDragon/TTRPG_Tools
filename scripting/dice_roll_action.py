from scripting.action import Action
import constants
import random

class DiceRollAction(Action):
    """Rolls one or many dice based on the requested input. Allow for standard dice sizes and custom dice."""

    def __init__(self):
        pass

    def execute(self, die_size, roll_modifier, min = -9999, max = 9999):
        """executes the dice roller action calls. min and max are not required to call and so ahve been added last."""

        """Check byt die size, have random pick a number, add the modifier, then check to make sure it is within the parameters.
        if too low, push the number to the lowest. If too high, push down to the highest."""
        out_list = []

        raw_outcome = random.randint(1, die_size)
        modified_outcome = raw_outcome + roll_modifier
        if modified_outcome > max:
            modified_outcome = max
        elif modified_outcome < min:
            modified_outcome = min

        out_list.append(raw_outcome)
        out_list.append(roll_modifier)
        out_list.append(modified_outcome)

        return out_list
        