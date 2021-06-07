import pygame


class ItemView:

    def __init__(self, x, y, w, h, item):
        self.item = item
        self.x = x
        self.y = y
        # width
        self.w = w
        # height
        self.h = h
        self.rect = pygame.rect.Rect(x, y, w, h)
