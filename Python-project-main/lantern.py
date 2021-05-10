
import pygame
from item import Item
class Lantern(Item):

    def __init__(self,capacity):
        super().__init__(Item.LANTERN)
        self.capacity=capacity