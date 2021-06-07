from objects.enemies.enemy import Enemy
import math
import random


class Skeleton(Enemy):

    def __init__(self, game, health, p_attack):
        super().__init__(game, health, p_attack)
        self.p_attack = p_attack

    def update(self):
        new_x = int(self.x + self.direction_x)
        new_y = int(self.y + self.direction_y)

        # nie wychodzi pozaplansze
        if new_x < 0:
            self.direction_x = 1
            new_x = self.x + self.direction_x
        elif new_x >= self.game.map.width:
            self.direction_x = -1
            new_x = self.x + self.direction_x
        if new_y < 0:
            self.direction_y = 1
            new_y = self.y + self.direction_y
        elif new_y >= self.game.map.height:
            self.direction_y = -1
            new_y = self.y + self.direction_y

        for obj in self.game.map.fields[new_x][new_y].objects:
            if self is obj:
                continue
            r = random.randint(0, 1)
            if r == 0:
                self.direction_x *= (-1)
            else:
                self.direction_y *= (-1)
            new_x = int(self.x + self.direction_x)
            new_y = int(self.y + self.direction_y)

        self.game.map.set_position(self, new_x, new_y)
        self.collect_collectibles()

    def move_toward_player(self, player, map):

        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist

        new_x = self.x + dx * self.velocity
        new_y = self.y + dy * self.velocity

        for obj in map.fields[int(new_x)][int(new_y)].objects:
            r = random.randint(0, 1)
            if r == 0:
                new_x = self.x
            else:
                new_y = self.y

        self.x = new_x
        self.y = new_y
        map.set_position(self, new_x, new_y)

    def skeleton_attack(self, player):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        for i in dx:
            flag = False
            for j in dy:
                if int(self.x) + dx[i] == int(player.x) and int(self.y) + dy[j] == int(player.y):
                    player.health -= int(5 / player.current_clothing.defence)
                    flag = True
                    break
            if flag:
                break
