from gameobject import GameObject
import pygame
import random
import math
from mineral import Mineral
from web import Web
#from bat import Bat
from classes import Player


class Enemy(GameObject):
    BAT = 0
    SPIDER = 1
    SKELETON = 2

    def __init__(self,game,health, p_attack):
        super().__init__(game,False)
        self.health=health
        self.p_attack=p_attack
        self.direction_x = -1
        self.direction_y = -1
        self.velocity=1
        #self.enemy_type = random.randint(0, 2)
        #self.rand_type()



    def draw(self, screen, x_center, y_center):
        if self.enemy_type==Enemy.BAT:
            screen.blit(self.game.graphics.bat_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type==Enemy.SPIDER:
            screen.blit(self.game.graphics.spider_texture, (x_center - 24, y_center - 24))
        elif self.enemy_type==Enemy.SKELETON:
            screen.blit(self.game.graphics.skeleton_texture, (x_center - 24, y_center - 24))

    #def hit_by_axe(self):
     #   self.health-=5
     #   print("hit by axe")

     #   if(self.health<=0):
     #       self.game.map.remove_game_object(self)

    #def rand_type(self):
    #    if enemy.type == 0:
    #        bat = Bat()

    def hit_by_weapon(self):

        self.health -= self.game.map.player.current_weapon.damage
        print("hit by weapon")
        print(self.health)
        if (self.health <= 0):
            self.game.map.remove_game_object(self)

    def check_if_in_map(self, p_x, p_y):
        if p_x < 0:
            self.direction_x = 1
            p_x = int(self.x + self.direction_x)
        elif p_x >= self.game.map.width:
            self.direction_x = -1
            p_x = int(self.x + self.direction_x)
        if p_y < 0:
            self.direction_y = 1
            p_y = int(self.y + self.direction_y)
        elif p_y >= self.game.map.height:
            self.direction_y = -1
            p_y = int(self.y + self.direction_y)
        return p_x, p_y

    def update(self):
        p_x = int(self.x + self.direction_x)
        p_y = int(self.y + self.direction_y)
        p_x, p_y = self.check_if_in_map(p_x, p_y)

        for obj in self.game.map.fields[p_x][p_y].objects:
            if not isinstance(obj, Player):

                r = random.randint(0, 1)
                if r == 0:
                    self.direction_x *= (-1)
                else:
                    self.direction_y *= (-1)
            p_x = int(self.x + self.direction_x)
            p_y = int(self.y + self.direction_y)
            p_x, p_y = self.check_if_in_map(p_x, p_y)

        self.game.map.set_position(self, p_x, p_y)




    def move_toward_player(self, player, map):

        dx,dy = player.x - self.x, player.y-self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist

        tmp_x = int(self.x + dx*self.velocity)
        tmp_y = int(self.y + dy*self.velocity)

        p_x = self.x + dx * self.velocity
        p_y = self.y + dy * self.velocity

        for obj in map.fields[tmp_x][tmp_y].objects:
            r = random.randint(0, 1)
            if r == 0:
                p_x = self.x
            else:
                p_y = self.y

        self.x = p_x
        self.y = p_y
        map.set_position(self, p_x, p_y)



    def skeleton_attack(self, player):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [ -1, -1, -1, 0, 0, 1, 1, 1]

        for i in dx:
            flag = False
            for j in dy:
                if int(self.x) + dx[i] == int(player.x) and int(self.y) + dy[j] == int(player.y):
                    player.health-=int(5/player.current_clothing.defence)
                    flag = True
                    break
            if flag:
                break
