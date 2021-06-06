import pygame
from weapon import Weapon


class Bow(Weapon):
    WOODEN = 1
    METAL = 2
    GOLD = 3
    EMERALD = 4
    DIAMOND = 5

    def __init__(self, category, damage, durability, type, radius):
        super().__init__(category, damage, durability)
        self.type = type
        self.radius = radius