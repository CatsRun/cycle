from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.cycle import Cycle 
import constants
from game.shared.point import Point
import random
from game.scripting.handle_collisions_action import HandleCollisionsAction

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
        cast = Cast()
        self.handle_collisions_action = HandleCollisionsAction()
        

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("scores1")
        food1 = cast.get_first_actor("foods1")
        cycle1 = cast.get_first_actor("cycles1")
        segments1 = cycle1.get_segments()
        messages = cast.get_actors("messages") #game over message

        score2 = cast.get_first_actor("scores2")
        food2 = cast.get_first_actor("foods2")
        cycle2 = cast.get_first_actor("cycles2")
        segments2 = cycle2.get_segments()
        # messages2 = cast.get_actors("messages2")#not declared

        x = int(constants.MAX_X - 900)
        y = int(constants.MAX_Y - 580)
        position = Point(x, y)

        #location of 2nd score 
        score2.set_position(position)
        
        #cycles stop growing when game is over
        # if self.handle_collisions_action._is_game_over == False:
            #cycles grow as they move as well as when they eat.
        # if (random.randint(1, 4) == 1): #change growth rate.
        #     cycle1.grow_tail(1) #slow the growth to a %
        #     cycle2.grow_tail(1) 

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food1) #why does this not interact with collisions?
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actors(messages, True)
        # self._video_service.flush_buffer()

        
        # self._video_service.clear_buffer()
        self._video_service.draw_actor(food2) #
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score2) #make this work
        # self._video_service.draw_actors(messages2, True) #not used
        self._video_service.flush_buffer()