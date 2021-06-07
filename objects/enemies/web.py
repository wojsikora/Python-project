import pygame
from gameobject import GameObject
from player import Player


class Web(GameObject):

    def __init__(self, game, direct_x, direct_y):
        super().__init__(game, False)
        self.direct_x = direct_x
        self.direct_y = direct_y

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.web_texture, (x_center - 24, y_center - 24))

    def update(self):

        self.x += self.direct_x
        self.y += self.direct_y

        if 0 <= self.x < self.game.map.width and self.x >= 0 and self.game.map.height:
            for obj in self.game.map.fields[int(self.x)][int(self.y)].objects:
                if isinstance(obj, GameObject):
                    if not isinstance(obj, Player):
                        self.game.map.remove_game_object(self)
                        return

        if self.x < 0:
            self.game.map.remove_game_object(self)

        elif self.x >= self.game.map.width:
            self.game.map.remove_game_object(self)

        elif self.y < 0:
            self.game.map.remove_game_object(self)

        elif self.y >= self.game.map.height:
            self.game.map.remove_game_object(self)
        elif int(self.x) == int(self.game.map.player.x) and int(self.y) == int(self.game.map.player.y):
            self.check_if_at_player_position(self.game.map.player)

        else:
            self.game.map.set_position(self, self.x, self.y)

    def hit_player(self, player):

        player.health -= int(10 / player.current_clothing.defence)

    def check_if_at_player_position(self, player):

        self.hit_player(player)
        self.game.map.remove_game_object(self)
