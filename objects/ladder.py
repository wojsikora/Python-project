from objects.gameobject import GameObject


class Ladder(GameObject):

    def __init__(self, game):
        super().__init__(game, False)

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.door_texture, (x_center - 24, y_center - 24))
