from enemy import Enemy
import pygame
import math
import random

class Skeleton(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)
        self.p_attack = p_attack


    def update(self):
        p_x = int(self.x + self.direction_x)
        p_y = int(self.y + self.direction_y)

        # nie wychodzi pozaplansze
        if p_x < 0:
            self.direction_x = 1
            p_x = self.x + self.direction_x
        elif p_x >= self.game.map.width:
            self.direction_x = -1
            p_x = self.x + self.direction_x
        if p_y < 0:
            self.direction_y = 1
            p_y = self.y + self.direction_y
        elif p_y >= self.game.map.height:
            self.direction_y = -1
            p_y = self.y + self.direction_y

        for obj in self.game.map.fields[p_x][p_y].objects:
            if self is obj:
                continue
            r = random.randint(0, 1)
            if r==0:
                self.direction_x *= (-1)
            else:
                self.direction_y *= (-1)
            p_x = int(self.x + self.direction_x)
            p_y = int(self.y + self.direction_y)

        self.game.map.set_position(self, p_x, p_y)
        self.collect_collectibles()

    def move_toward_player(self, player, map):

        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist

        tmp_x = int(self.x + dx * self.velocity)
        tmp_y = int(self.y + dy * self.velocity)

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


