import pygame
from gameobject import GameObject
from classes import Player

class Web(GameObject):

    def __init__(self, game, dir_x, dir_y):
        super().__init__(game, False)
        self.dir_x = dir_x
        self.dir_y = dir_y

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.web_texture, (x_center - 24, y_center - 24))



    def update(self):

        self.x += self.dir_x
        self.y += self.dir_y


        if self.x < 0:
            self.game.map.remove_game_object(self)

        elif self.x >= self.game.map.width:
            self.game.map.remove_game_object(self)

        elif self.y < 0:
            self.game.map.remove_game_object(self)

        elif self.y >= self.game.map.height:
            self.game.map.remove_game_object(self)
        else:
            self.game.map.set_position(self, self.x, self.y)

    def hit_player(self, player):
        player.health-=10


    def check_if_at_player_position(self, player):

        if int(self.x) == int(player.x) and int(self.y) == int(player.y):
            self.hit_player(player)
            self.game.map.remove_game_object(self)
