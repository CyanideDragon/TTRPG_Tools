class Director:
    '''The director of the game.
    
    The responsibility of the Director is to dictate and control the sequence of actions.
    
    Attributes:
        _video_service (VideoService): Provides the GUI output.

    '''
    
    def __init__(self, video_service):
        '''Constructs a new director using the video service.
        
        Args:
            video_service (VideoService): an instance of the video service.'''
        
        self._video_service = video_service

    def start_game(self):
        '''Starts the game given cast and script, running the main game loop
        
        args:
            cast (Cast): the cast of actors.
            script(Script): the script of actions'''

        ###### Cast and Script will be implemented in time. Delete once implemented.
        
        self._video_service.open_window() 
        '''Calls to the video services open_window funciton'''
        while self._video_service.is_window_open():
            self._video_service.clear_buffer()
            self._video_service.flush_buffer()
            #Clear and flush buffer must be removed and moved to a scripting action, such as drawing actors during a more complete implementation. 

        self._video_service.close_window()
        '''Calls to the video services close_window funciton'''
    
    def _execute_actions(self):
        '''calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): the cast of actors.
            script (Script): the script of actors.
            '''
        ###### group, cas, script all need to be implemented in time. Delete once implemented.

        pass