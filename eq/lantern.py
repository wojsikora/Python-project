import pygame
from item import Item


class Lantern(Item):

    def __init__(self, capacity, image, price):
        super().__init__(Item.LANTERN, price)
        self.capacity = capacity
        self.image = image
