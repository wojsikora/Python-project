import pygame
from weapon import Weapon


class Sword(Weapon):
    FIST = 0
    METAL = 1
    GOLD = 2
    EMERALD = 3
    DIAMOND = 4

    def __init__(self, category, damage, durability, type):
        super().__init__(category, damage, durability)
        self.type = type