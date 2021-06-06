from enemy import Enemy
import pygame
import math
from web import Web

class Spider(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)
        #self.p_attack = 15

    def web_attack(self, player, webs):
        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist

        if (dist <= 5):
            web = Web(self.game, int(dx * self.velocity), int(dy * self.velocity))
            webs.append(web)
            web.x = int(self.x)
            web.y = int(self.y)
            web.dir_x = (dx * self.velocity)
            web.dir_y = (dy * self.velocity)
            web.x = int(self.x) + web.dir_x
            web.y = int(self.y) + web.dir_y
            self.game.map.set_position(web, web.x, web.y)
