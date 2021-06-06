import pygame
from clothing import Clothing


class Chestplate(Clothing):
    NOTHING = 0
    LEATHER = 1
    METAL = 2
    GOLD = 3
    EMERALD = 4
    DIAMOND = 5

    def __init__(self, type, protection, durability):
        super().__init__()
        self.type = type
        self.protection = protection
        self.durability = durability
