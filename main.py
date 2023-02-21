import constants
from shared.point import Point
from directing.director import Director
"""All services must be called"""
from services.keyboard_service import KeyboardService
from services.mouse_service import MouseService
from services.video_service import VideoService
"""All scripting but action must be called"""
from scripting.script import Sctript
from scripting.button_action import ButtonAction
from scripting.character_action import CharacterAction
from scripting.control_actor_action import ControlActorAction
from scripting.draw_actor_action import DrawActorsAction
from scripting.drop_down_action import DropDownAction
from scripting.input_box_action import InputBoxAction
from scripting.map_action import MapAction
from scripting.menu_action import MenuAction
from scripting.move_actor_action import MoveActorsAction
from scripting.non_playable_character_action import NonPlayableCharacterAction
from scripting.playable_character_action import PlableCharacterAction
from scripting.token_action import TokenAction
from scripting.create_inventory_items import CreateInventoryItems
from scripting.do_weapon_item_action import DoWeaponItemAction
#Add Actors as necessary if they need to be called on initialization below cast
from casting.cast import Cast
from casting.menu import Menu
from casting.drop_down import DropDown
from casting.button import Button

def main():

    """create the cast"""
    cast = Cast()

    keyboard_service = KeyboardService()
    #video service should pass in thing only if needed. Everything else should be pulled from constants
    video_service = VideoService() 
    mouse_service = MouseService()

    script = Sctript()

    #Make sure we know what we need to pass into all the scripts
    button_action = ButtonAction()
    character_action = CharacterAction()
    # control_actor_action = ControlActorAction(keyboard_service, mouse_service)
    # draw_actor_action = DrawActorsAction(video_service)
    # drop_down_action = DropDownAction(mouse_service)
    # input_box_action = InputBoxAction(keyboard_service)
    map_action = MapAction()
    # menu_action = MenuAction(mouse_service)
    move_actor_action = MoveActorsAction()
    non_playable_character_action = NonPlayableCharacterAction()
    playable_character_action = PlableCharacterAction()
    token_action = TokenAction()



    #add script executions here

    script.add_action("input", button_action)
    script.add_action("input", character_action)
    # script.add_action("input", control_actor_action)
    # script.add_action("input", drop_down_action)
    # script.add_action("input", input_box_action)
    script.add_action("input", map_action)
    # script.add_action("input", menu_action)
    script.add_action("input", move_actor_action)
    script.add_action("input", non_playable_character_action)
    script.add_action("input", playable_character_action)
    script.add_action("input", token_action)
    # script.add_action("output", draw_actor_action)


    director = Director()
    director.start_game(cast, script)




if __name__ == "__main__":
    main()