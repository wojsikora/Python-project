from surface import Surface
import time


class Lava(Surface):

    def __init__(self, game):
        super().__init__(game, self)

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.lava_texture, (x_center - 24, y_center - 24))

    def player_on(self, player):
        dx = [0, 0, -1, 1, 0]
        dy = [-1, 0, 0, 0, 1]
        flag = False
        for i in dx:
            for j in dy:
                if int(self.x) + i == int(player.x) and int(self.y) + j == int(player.y):
                    flag = True

        if flag:
            player.health -= 1
