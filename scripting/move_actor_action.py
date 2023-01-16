from scripting.action import Action
import constants

class MoveActorsAction(Action):
    """Moves the actors. 
    
    The responsibility of a KeyboardService is to detect user key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        pass

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._move_menu(cast)
        self._move_drop_down(cast)
        self._move_button(cast)
        self._move_input_box(cast)
        self._move_map(cast)
        self._move_character(cast)
        self._move_non_playable_character(cast)
        self._move_playable_character(cast)
        self._move_token(cast)

    def _move_menu(self, cast):
        menu = cast.get_first_actor("menu")
        menu.move_next(constants.MAX_X, constants.MAX_Y, 'menu')

    def _move_button(self, cast):
        button = cast.get_first_actor("button")
        button.move_next(constants.MAX_X, constants.MAX_Y, 'button')

    def _move_drop_down(self, cast):
        drop_down = cast.get_first_actor("drop_down")
        drop_down.move_next(constants.MAX_X, constants.MAX_Y, 'drop_down')
    
    def _move_input_box(self, cast):
        input_box = cast.get_first_actor("input_box")
        input_box.move_next(constants.MAX_X, constants.MAX_Y, 'input_box')

    def _move_map(self, cast):
        game_map = cast.get_first_actor("game_map")
        game_map.move_next(constants.MAX_X, constants.MAX_Y, 'game_map')
    
    def _move_character(self, cast):
        character = cast.get_first_actor("character")
        character.move_next(constants.MAX_X, constants.MAX_Y, 'character')
    
    def _move_non_playable_character(self, cast):
        non_playable_character = cast.get_first_actor("non_playable_character")
        non_playable_character.move_next(constants.MAX_X, constants.MAX_Y, 'non_playable_character')

    def _move_playable_character(self, cast):
        playable_character = cast.get_first_actor("playable_character")
        playable_character.move_next(constants.MAX_X, constants.MAX_Y, 'playable_character')
    
    def _move_game_token(self, cast):
        game_token = cast.get_first_actor("game_token")
        game_token.move_next(constants.MAX_X, constants.MAX_Y, 'game_token')