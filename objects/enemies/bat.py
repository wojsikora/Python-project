
import pygame

from objects.enemies.enemy import Enemy


class Bat(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)

    def bat_attack(self, player):
        if int(self.x) == int(player.x) and int(self.y) == int(player.y):
            player.health -= int(5/player.current_clothing.defence)
