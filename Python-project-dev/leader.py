import pygame.rect

from gameobject import GameObject
class Leader(GameObject):

    def __init__(self, game):
        super().__init__(game, False)

    def draw(self,screen,x_center,y_center):

        #rect=pygame.rect.Rect(x_center,y_center,48,48)
        #pygame.draw.rect(screen,(100,100,100),rect)
        screen.blit(self.game.graphics.door_texture, (x_center - 24, y_center - 24))