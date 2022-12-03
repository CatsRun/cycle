import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.scripting.control_actors_action import ControlActorsAction


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
        _cycle_color: 
    """
    def __init__(self, color):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        self._prepare_body()
        # self.cycle1 = cycle1
        # player1 = self
        # player2 = self

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            # segment.set_color(constants.GREEN) #this color needs to change depentand upon each player
            segment.set_color(self._cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    # def _prepare_body(self, change_start_point):
    def _prepare_body(self):
        # a = change_start_point
        x = int(constants.MAX_X / 2) #start location of snake
        y = int(constants.MAX_Y / 2)
        # x = int(constants.MAX_X / 2 + a)
        # # x = self.position 
        # y = int(constants.MAX_Y / 2 + a)


        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else self._cycle_color #this sets the color of the body to the color in main that is passed here
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

