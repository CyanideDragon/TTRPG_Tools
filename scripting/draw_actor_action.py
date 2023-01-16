from scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()
        self._draw_menu(cast)
        self._draw_drop_down(cast)
        self._draw_button(cast)
        self._draw_input_box(cast)
        self._draw_map(cast)
        self._draw_character(cast)
        self._draw_non_playable_character(cast)
        self._draw_playable_character(cast)
        self._draw_token(cast)
        self._video_service.flush_buffer()

    def _draw_menu(self, cast):
        menu = cast.get_first_actor("menu")
        self._video_service.draw_actor(menu)
    
    def _draw_drop_down(self, cast):
        drop_down = cast.get_first_actor("drop_down")
        self._video_service.draw_actor(drop_down)

    def _draw_button(self, cast):
        button = cast.get_first_actor("button")
        self._video_service.draw_actor(button)

    def _draw_input_box(self, cast):
        input_box = cast.get_first_actor("input_box")
        self._video_service.draw_actor(input_box)

    def _draw_map(self, cast):
        game_map = cast.get_first_actor("game_map")
        self._video_service.draw_actor(game_map)

    def _draw_character(self, cast):
        character = cast.get_first_actor("character")
        self._video_service.draw_actor(character)

    def _draw_non_playable_character(self, cast):
        non_playable_character = cast.get_first_actor("non_playable_character")
        self._video_service.draw_actor(non_playable_character)

    def _draw_playable_character(self, cast):
        playable_character = cast.get_first_actor("playable_character")
        self._video_service.draw_actor(playable_character)

    def _draw_token(self, cast):
        game_token = cast.get_first_actor("game_token")
        self._video_service.draw_actor(game_token)
    
