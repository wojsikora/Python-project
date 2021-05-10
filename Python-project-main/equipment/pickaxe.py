import pygame
from clothing import Clothing


class Pickaxe(Clothing):
    WOODEN = 1
    METAL = 2
    GOLD = 3
    EMERALD = 4
    DIAMOND = 5

    def __init__(self, type, mining, durability):
        super().__init__()
        self.type = type
        self.mining = mining
        self.durability = durability