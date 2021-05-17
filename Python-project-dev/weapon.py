
import pygame
from item import Item
class Weapon(Item):

    def __init__(self,damage):
        super().__init__(Item.WEAPON)
        self.damage=damage
