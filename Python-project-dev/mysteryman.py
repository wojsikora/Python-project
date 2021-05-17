import random
from gameobject import GameObject
import pygame
from lantern import Lantern
from weapon import Weapon
from scene import ShopScene
from pickaxe import Pickaxe
from graphics import Graphics
class MysteryMan(GameObject):

    def __init__(self,game):
        super().__init__(game,False)
        self.goods=[]
        self.goods.append(Pickaxe(20,game.graphics.cobelstone_pickaxe,1))
        self.goods.append(Pickaxe(40,game.graphics.diamond_pickaxe,2))
        self.goods.append(Pickaxe(60,game.graphics.golden_pickaxe,3))
        self.goods.append(Pickaxe(80,game.graphics.iron_pickaxe,4))
        self.goods.append(Lantern(40,game.graphics.lantern_texture,5))
        # for i in range(11):
        #     if i<5:
        #         self.goods.append(Lantern((i+1)*20))
        #     else:
        #         self.goods.append(Weapon((i+1)*20))


    def trade(self):
        print("trading")
        #pozycja do wyswietlenia mineralu



    def generate_position():
        while 1:
            x=random.randint(0,self.game.map.width)
            y=random.randint(0,self.game.map.height)
            if len(self.game.map.fields[x][y].objects)==0:
                self.game.map.set_position(self,x,y)

    def draw(self,screen,x_center,y_center):
        #rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
        #pygame.draw.rect(screen,(255, 26, 180),rect)
        screen.blit(self.game.graphics.merchant_texture, (x_center - 15, y_center - 15))
