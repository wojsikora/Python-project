from enemy import Enemy
import pygame


class Bat(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)
        #self.p_attack = 10
        #self.health = 5

    def bat_attack(self, player):
        if int(self.x) == int(player.x) and int(self.y) == int(player.y):
            player.health-=5


