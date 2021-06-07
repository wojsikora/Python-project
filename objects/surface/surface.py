from objects.gameobject import GameObject


class Surface(GameObject):

    def __init__(self, game, type):
        super().__init__(game, False)
