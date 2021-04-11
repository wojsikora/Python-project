from gameobject import GameObject
import pygame
import random


class Enemy(GameObject):
    BAT = 0
    SPIDER = 1
    SKELETON = 2

    def __init__(self,game,health, p_attack):
        super().__init__(game,False)
        self.health=health
        self.p_attack=p_attack
        self.enemy_type = random.randint(0, 2)



    def draw(self, screen, x_center, y_center):
        if self.enemy_type==Enemy.BAT:
            screen.blit(self.game.graphics.bat_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type==Enemy.SPIDER:
            screen.blit(self.game.graphics.spider_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type==Enemy.SKELETON:
            screen.blit(self.game.graphics.skeleton_texture, (x_center - 24, y_center - 24))

    def hit_by_axe(self):
        self.health-=5
        print("hit by axe")

        if(self.health<=0):
            self.game.map.remove_game_object(self)