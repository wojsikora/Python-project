import pygame
import random
from objects.gameobject import GameObject
from objects.rocks.mineral import Mineral


class Rock(GameObject):
    # #1,0
    # GOLD=0
    # COPPER=1
    # EMERALD=2
    # DIAMOND=3
    # BEDROCK=4

    def __init__(self, game, destructable, screen, contains_minerals):
        super().__init__(game, False)
        self.screen = screen
        self.destructable = destructable
        self.contains_minerals = contains_minerals
        if destructable and contains_minerals:
            self.mineral_type = random.randint(0, 4)
        else:
            self.mineral_type = None
        self.durability_factor = 2
        self.set_durability()

    def set_durability(self):
        if self.mineral_type == 0:
            self.durability = 1000 * self.durability_factor
        elif self.mineral_type == 1:
            self.durability = 500 * self.durability_factor
        elif self.mineral_type == 2:
            self.durability = 1500 * self.durability_factor
        elif self.mineral_type == 3:
            self.durability = 2000 * self.durability_factor
        elif self.mineral_type is None:
            self.durability = 300 * self.durability_factor

    def draw(self, screen, x_center, y_center):
        if self.mineral_type == Mineral.GOLD:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (255, 233, 0), rect)
        elif self.mineral_type == Mineral.COPPER:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (220, 127, 100), rect)
        elif self.mineral_type == Mineral.EMERALD:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (80, 220, 100), rect)
        elif self.mineral_type == Mineral.DIAMOND:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (185, 242, 255), rect)
        elif self.mineral_type == Mineral.BEDROCK:
            screen.blit(self.game.graphics.bedrock_texture, (x_center - 24, y_center - 24))
        elif self.mineral_type is None:
            rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
            pygame.draw.rect(screen, (40, 40, 100), rect)

    def hit_by_axe(self):


        # pozycja do wyswietlenia mineralu
        if self.mineral_type != 4:
            pos_x = self.x
            pos_y = self.y
            self.durability -= self.game.map.player.current_pickaxe.power

            if self.durability <= 0:

                self.game.map.remove_game_object(self)
                if self.mineral_type is not None:
                    mineral = Mineral(self.game, self.mineral_type)
                    self.game.map.add_mineral(mineral)
                    self.game.map.set_position(mineral, pos_x, pos_y)

    def hit_by_weapon(self):
        pass
