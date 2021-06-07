from gameobject import GameObject
import pygame
import random
import math
from mineral import Mineral
from web import Web
# from bat import Bat
from player import Player


class Enemy(GameObject):
    BAT = 0
    SPIDER = 1
    SKELETON = 2

    def __init__(self, game, health, p_attack):
        super().__init__(game, False)
        self.enemy_type = None
        self.health = health
        self.p_attack = p_attack
        self.direction_x = -1
        self.direction_y = -1
        self.velocity = 1

    def draw(self, screen, x_center, y_center):
        if self.enemy_type == Enemy.BAT:
            screen.blit(self.game.graphics.bat_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type == Enemy.SPIDER:
            screen.blit(self.game.graphics.spider_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type == Enemy.SKELETON:
            screen.blit(self.game.graphics.skeleton_texture, (x_center - 24, y_center - 24))

    # def hit_by_axe(self):
    #   self.health-=5
    #   print("hit by axe")

    #   if(self.health<=0):
    #       self.game.map.remove_game_object(self)

    # def rand_type(self):
    #    if enemy.type == 0:
    #        bat = Bat()

    def hit_by_weapon(self):

        self.health -= self.game.map.player.current_weapon.damage
        print("hit by weapon")
        print(self.health)
        if self.health <= 0:
            self.game.map.remove_game_object(self)

    def check_if_in_map(self, new_x, new_y):
        if new_x < 0:
            self.direction_x = 1
            new_x = int(self.x + self.direction_x)
        elif new_x >= self.game.map.width:
            self.direction_x = -1
            new_x = int(self.x + self.direction_x)
        if new_y < 0:
            self.direction_y = 1
            new_y = int(self.y + self.direction_y)
        elif new_y >= self.game.map.height:
            self.direction_y = -1
            new_y = int(self.y + self.direction_y)
        return new_x, new_y

    def update(self):
        new_x = int(self.x + self.direction_x)
        new_y = int(self.y + self.direction_y)
        new_x, new_y = self.check_if_in_map(new_x, new_y)

        for obj in self.game.map.fields[new_x][new_y].objects:
            if not isinstance(obj, Player):

                r = random.randint(0, 1)
                if r == 0:
                    self.direction_x *= (-1)
                else:
                    self.direction_y *= (-1)
            new_x = int(self.x + self.direction_x)
            new_y = int(self.y + self.direction_y)
            new_x, new_y = self.check_if_in_map(new_x, new_y)

        self.game.map.set_position(self, new_x, new_y)
