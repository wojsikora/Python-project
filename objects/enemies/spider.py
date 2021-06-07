from objects.enemies.enemy import Enemy
import math
from objects.enemies.web import Web


class Spider(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)

    def web_attack(self, player, webs):
        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist

        if dist <= 5:
            web = Web(self.game, int(dx * self.velocity), int(dy * self.velocity))
            webs.append(web)
            web.x = int(self.x)
            web.y = int(self.y)
            web.direct_x = (dx * self.velocity)
            web.direct_y = (dy * self.velocity)
            web.x = int(self.x) + web.direct_x
            web.y = int(self.y) + web.direct_y
            self.game.map.set_position(web, web.x, web.y)
