import pygame

from eq.item import Item


class Weapon(Item):

    def __init__(self, damage, image, price):
        super().__init__(Item.WEAPON, price)
        self.damage = damage
        self.image = image
