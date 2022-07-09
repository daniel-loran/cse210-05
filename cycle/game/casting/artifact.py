from game.casting.actor import Actor
from game.shared.color import Color


class Artifact(Actor):
    # Places an artifact trail behind the actor. The artifact trail is a list of '#' characters.

    BLUE = Color(0, 0, 255)
    YELLOW = Color(255, 255, 0)

    def __init__(self):
        super().__init__()