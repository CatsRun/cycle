import constants 
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle import Cycle

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        score1 = cast.get_first_actor("scores1")
        # food = cast.get_first_actor("foods") 
        cycle1 = cast.get_first_actor("cycles1")
        head1 = cycle1.get_head()                 
        
        score2 = cast.get_first_actor("scores2")
        food = cast.get_first_actor("foods2")
        cycle2 = cast.get_first_actor("cycles2")
        head2 = cycle2.get_head()

        if head1.get_position().equals(food.get_position()):
            points = food.get_points()
            cycle1.grow_tail(points)
            score1.add_points(points)
            food.reset()

        if head2.get_position().equals(food.get_position()):
            points = food.get_points()
            cycle2.grow_tail(points)
            score2.add_points(points)
            food.reset()



    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycles1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]

        cycle2 = cast.get_first_actor("cycles2")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments1: #this checks if head collides with segments from cycle1
            if head1.get_position().equals(segment.get_position()): #or head2 = segment1 or head1 = segment2 or head 2 = segment2
                self._is_game_over = True
            elif head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head1.get_position().equals(head2.get_position()):
                self._is_game_over = True

        for segment in segments2: #this check if heads collide with segments from cycle2
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycles1")
            segments1 = cycle1.get_segments()
            food1 = cast.get_first_actor("foods1")
            score1 = cast.get_first_actor("scores1")
            score2 = cast.get_first_actor("scores2")
            winner = ''
            food2 = cast.get_first_actor("foods2")
            cycle2 = cast.get_first_actor("cycles2")
            segments2 = cycle2.get_segments()

            # #change game over message depentent upon winner
            # if 'score2' > 'score1':
            #     # winner = constants.RED
            #     winner = 'RED won!'
            # elif 'score1' < 'score2':
            #     # winner = constants.GREEN
            #     winner = 'GREEN won!'
            # else:
            #     winner = 'Tie'

            #cycles stop growing when game is over
            # cycle1.grow_tail(0) 
            # cycle2.grow_tail(0) 

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            # message.set_text(f"Game Over! {winner}") #when conditional winner statemnt works, uncoment this
            message.set_position(position) #position of end message
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)
            food1.set_color(constants.WHITE)
            
            for segment in segments2:
                segment.set_color(constants.WHITE)
            food2.set_color(constants.WHITE)
