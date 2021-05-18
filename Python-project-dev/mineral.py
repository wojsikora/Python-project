import pygame
from gameobject import GameObject

class Mineral(GameObject):
    GOLD = 0
    COPPER = 1
    EMERALD = 2
    DIAMOND = 3
    BEDROCK = 4
    def __init__(self,game,mineral_type):
        super().__init__(game,True)
        self.mineral_type=mineral_type

    def draw(self,screen,x_center,y_center):
        if self.mineral_type==Mineral.GOLD:
            # rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
            # pygame.draw.rect(screen, (255, 233,0),rect)
            screen.blit(self.game.graphics.gold_texture,(x_center-24,y_center-24))
        elif self.mineral_type==Mineral.COPPER:
            #rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
            #pygame.draw.rect(screen,(220,127,100),rect)
            screen.blit(self.game.graphics.copper_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type==Mineral.EMERALD:
            # rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            screen.blit(self.game.graphics.emerald_texture,(x_center-24,y_center-24))
            #pygame.draw.rect(screen, (80, 220, 100), rect)
        elif self.mineral_type == Mineral.DIAMOND:
            #rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            screen.blit(self.game.graphics.diamond_texture,(x_center-24,y_center-24))
        #elif self.mineral_type == Mineral.BEDROCK:
        #    rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
        #    pygame.draw.rect(screen, (0, 0,0), rect)
        elif self.mineral_type==None:
            rect=pygame.rect.Rect(x_center-24,y_center-24,48,48)
            pygame.draw.rect(screen,(40,40,100),rect)
