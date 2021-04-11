from enemy import Enemy
import pygame


class Spider(Enemy):

    def __init__(self):
        super().__init__(game, 25)
        self.p_attack = 15

