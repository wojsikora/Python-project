import pygame
from clothing import Clothing


class Weapon(Clothing):
    SWORD = 0
    BOW = 1

    def __init__(self, category, damage, durability):
        super().__init__()
        self.category = category
        self.damage = damage
        self.durability = durability