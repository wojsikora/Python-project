import random
from gameobject import GameObject
import pygame
class MysteryMan(GameObject):

    def __init__(self,game):
        super().__init__(game,False)
        self.goods=[]

    def generate_position():
        while 1:
            x=random.randint(0,self.game.map.width)
            y=random.randint(0,self.game.map.height)
            if len(self.game.map.fields[x][y].objects)==0:
                self.game.map.set_position(self,x,y)

    def draw(self,screen,x_center,y_center):
        rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
        pygame.draw.rect(screen,(255, 26, 180),rect)
