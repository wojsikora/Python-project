import pygame
from clothing import Clothing


class Helmet(Clothing):
    SHORT = 0
    MEDIUM = 1
    LONG = 2

    def __init__(self, type, radius, durability):
        super().__init__()
        self.type = type
        self.radius = radius
        self.durability = durability
