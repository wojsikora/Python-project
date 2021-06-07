import random
from gameobject import GameObject
from eq.pickaxe import Pickaxe
from eq.weapon import Weapon
from eq.clothing import Clothing


class MysteryMan(GameObject):

    def __init__(self, game):
        super().__init__(game, False)
        self.goods = []
        self.goods.append(Pickaxe(20, game.graphics.cobelstone_pickaxe, 1))
        self.goods.append(Pickaxe(80, game.graphics.diamond_pickaxe, 2))
        self.goods.append(Pickaxe(60, game.graphics.golden_pickaxe, 3))
        # self.goods.append(Pickaxe(80,game.graphics.iron_pickaxe,4))
        # self.goods.append(Lantern(40,game.graphics.lantern_texture,5))
        self.goods.append(Clothing(2, self.game.graphics.armor2_texture, 5))
        self.goods.append(Weapon(10, game.graphics.sword_texture, 10))

    def trade(self):
        print("trading")
        # pozycja do wyswietlenia mineralu

    def generate_position(self):
        while True:
            x = random.randint(0, self.game.map.width)
            y = random.randint(0, self.game.map.height)
            if len(self.game.map.fields[x][y].objects) == 0:
                self.game.map.set_position(self, x, y)

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.merchant_texture, (x_center - 15, y_center - 15))
