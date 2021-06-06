import pygame
from item import Item

class Clothing(Item):

    def __init__(self, defence, image, price):
        super().__init__(Item.CLOTHING, price)
        self.defence=defence
        self.image = image
