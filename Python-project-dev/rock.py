import pygame
import random
from gameobject import GameObject
from mineral import Mineral

class Rock(GameObject):
    # #1,0
    # GOLD=0
    # COPPER=1
    # EMERALD=2
    # DIAMOND=3
    # BEDROCK=4


    def __init__(self,game,destructable,screen,contains_minerals):
        super().__init__(game,False)
        self.screen=screen
        self.indestructable_rock=pygame.image.load('images/bedrocktexture.bmp')
        self.destructable=destructable
        self.contains_minerals=contains_minerals
        if destructable and contains_minerals:
            self.mineral_type=random.randint(0,4)
        else:
            self.mineral_type=None

    # def blitme(self,pos_x,pos_y):
    #     self.rect=pygame.rect.Rect()
    #     self.rect.x=pos_x
    #     self.rect.y=pos_y
    #     self.screen.blit(self.indestructable_rock,self.rect)


    def draw(self,screen,x_center,y_center):
        if self.mineral_type==Mineral.GOLD:
            rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
            pygame.draw.rect(screen, (255, 233,0),rect)
        elif self.mineral_type==Mineral.COPPER:
            rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
            pygame.draw.rect(screen,(220,127,100),rect)
        elif self.mineral_type==Mineral.EMERALD:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (80, 220, 100), rect)
        elif self.mineral_type == Mineral.DIAMOND:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (185,242,255), rect)
        elif self.mineral_type ==Mineral.BEDROCK:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (0, 0,0), rect)
        elif self.mineral_type==None:
            rect=pygame.rect.Rect(x_center-24,y_center-24,48,48)
            pygame.draw.rect(screen,(40,40,100),rect)


    def hit_by_axe(self):
        print("hit by axe")
        #pozycja do wyswietlenia mineralu
        pos_x=self.x
        pos_y=self.y
        self.game.map.remove_game_object(self)
        if self.mineral_type!=None:
            mineral=Mineral(self.game,self.mineral_type)
            self.game.map.add_mineral(mineral)
            self.game.map.set_position(mineral,pos_x,pos_y)

    def hit_by_weapon(self):
        pass

