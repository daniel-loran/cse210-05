from game.casting.actor import Actor
from game.shared.color import Color


class Artifact(Actor):
    # Places an artifact trail behind the actor. The artifact trail is a list of '#' characters.

    BLUE = Color(0, 0, 255)

    def __init__(self):
        super().__init__()


    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(Artifact.BLUE)
            self._segments.append(segment)