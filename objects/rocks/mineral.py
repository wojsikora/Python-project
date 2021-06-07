import pygame
from gameobject import GameObject


class Mineral(GameObject):
    GOLD = 0
    COPPER = 1
    EMERALD = 2
    DIAMOND = 3
    BEDROCK = 4

    def __init__(self, game, mineral_type):
        super().__init__(game, True)
        self.mineral_type = mineral_type

    def draw(self, screen, x_center, y_center):
        if self.mineral_type == Mineral.GOLD:
            screen.blit(self.game.graphics.gold_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type == Mineral.COPPER:
            screen.blit(self.game.graphics.copper_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type == Mineral.EMERALD:
            screen.blit(self.game.graphics.emerald_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type == Mineral.DIAMOND:
            screen.blit(self.game.graphics.diamond_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type is None:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (40, 40, 100), rect)
