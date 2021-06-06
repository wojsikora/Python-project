
import pygame

class Item:
    LANTERN=1
    WEAPON=2
    PICKAXE=3
    CLOTHING = 4
    def __init__(self,type,price):
        self.type=type
        self.price=price
