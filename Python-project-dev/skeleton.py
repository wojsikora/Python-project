from enemy import Enemy
import pygame
import math

class Skeleton(Enemy):

    def __init__(self):
        super().__init__(game, 25)
        self.p_attack = 20


    def update(self):
        p_x = int(self.x + self.direction_x)
        p_y = int(self.y + self.direction_y)

        # nie wychodzi pozaplansze
        if p_x < 0:
            self.direction_x = 1
            p_x = self.x + self.direction_x
        elif p_x >= self.game.map.width:
            self.direction_x = -1
            p_x = self.x + self.direction_x
        if p_y < 0:
            self.direction_y = 1
            p_y = self.y + self.direction_y
        elif p_y >= self.game.map.height:
            self.direction_y = -1
            p_y = self.y + self.direction_y

        for obj in self.game.map.fields[p_x][p_y].objects:
            if self is obj:
                continue
            r = random.randint(0, 1)
            if r==0:
                self.direction_x *= (-1)
            else:
                self.direction_y *= (-1)
            p_x = int(self.x + self.direction_x)
            p_y = int(self.y + self.direction_y)

        self.game.map.set_position(self, p_x, p_y)
        self.collect_collectibles()

    def move_toward_player(self, player):
        dx,dy = player.x - self.x, player.y-self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.x += dx*self.velocity #utworz velocity dla Enemy
        self.y += dy*self.velocity


