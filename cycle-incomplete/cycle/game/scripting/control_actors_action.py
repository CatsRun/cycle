import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cast import Cast

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0) #change the start position
        self.cast2 = Cast()



    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # if constants.RED:  #sets 1st, or RED snake to wsad keys
        # if self.cycle == 1:
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        cycle = cast.get_first_actor("cycles")
        cycle.turn_head(self._direction1)


        # else: #sets other snake to jlik keys  #how do I set this to the 2nd snake?
        # if cycle.get_player == 2:
    # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            
        cycle2 = cast.get_first_actor("cycles") #tried this as 2nd actor. Needed to add get_2nd_ to cycle class. How can I add a 2nd snake and assign it these comands?
        cycle2.turn_head(self._direction2)