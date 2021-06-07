import pygame
from map import Map
from graphics import Graphics
import sys
from GUI.level_information import LevelInformation
from objects.ladder import Ladder
from objects.mysteryman import MysteryMan


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Miner")
        self.graphics = Graphics()
        self.lvl_info = LevelInformation()
        self.level = 1
        self.map = Map(self, 25, 18, 5, 0, self.screen)
        self.ran = 0
        self.pop_up = None
        self.clicked_x = None
        self.clicked_y = None

    def run_game(self):
        self.map.generate_rocks()

        while True:
            # Oczekiwanie na nacisniecie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_mouse_pressed(event)

            self.update(14)
            self._update_screen()

    def _update_screen(self):

        self.screen.fill((200, 200, 200))

        if self.pop_up is None:
            for rock in self.map.rocks:
                # wymiar w pikselach
                rock.draw(self.screen, rock.x * 50, rock.y * 50)
            for bat in self.map.bats:
                bat.draw(self.screen, bat.x * 50, bat.y * 50)
            for spider in self.map.spiders:
                spider.draw(self.screen, spider.x * 50, spider.y * 50)
            for skeleton in self.map.skeletons:
                skeleton.draw(self.screen, skeleton.x * 50, skeleton.y * 50)
            self.map.player.draw(self.screen, self.map.player.x * 50, self.map.player.y * 50)
            for mineral in self.map.minerals:
                mineral.draw(self.screen, mineral.x * 50, mineral.y * 50)
            for m in self.map.MM:
                m.draw(self.screen, m.x * 50, m.y * 50)
            for w in self.map.webs:
                w.draw(self.screen, w.x * 50, w.y * 50)
            for ladder in self.map.ladders:
                ladder.draw(self.screen, ladder.x * 50, ladder.y * 50)
            for water in self.map.water:
                water.draw(self.screen, water.x * 50, water.y * 50)
            for lava in self.map.lava:
                lava.draw(self.screen, lava.x * 50, lava.y * 50)
        else:
            self.pop_up.draw()
            if self.clicked_x is not None and self.clicked_y is not None:
                self.pop_up.check_clicked_field(self.clicked_x, self.clicked_y)

        pygame.display.flip()

    def check_keydown(self, event):
        player = self.map.get_player()
        if event.key == pygame.K_LEFT:
            player.velocity_x = -1
        elif event.key == pygame.K_RIGHT:
            player.velocity_x = 1
        elif event.key == pygame.K_DOWN:
            player.velocity_y = 1
        elif event.key == pygame.K_UP:
            player.velocity_y = -1
        elif event.key == pygame.K_a:
            self.map.player.pressed_axe = True
        elif event.key == pygame.K_d:
            self.map.player.pressed_weapon = True
        elif event.key == pygame.K_h:
            self.map.player.pressed_handel = True
        elif event.key == pygame.K_s:
            self.map.player.pressed_enter_next_level = True
        elif event.key == pygame.K_t:
            self.map.player.pressed_drink = True
        elif event.key == pygame.K_q:
            self.pop_up = None

    def check_keyup(self, event):
        player = self.map.get_player()
        if event.key == pygame.K_LEFT:
            player.velocity_x = 0
        elif event.key == pygame.K_RIGHT:
            player.velocity_x = 0
        elif event.key == pygame.K_DOWN:
            player.velocity_y = 0
        elif event.key == pygame.K_UP:
            player.velocity_y = 0
        elif event.key == pygame.K_a:
            self.map.player.pressed_axe = False
        elif event.key == pygame.K_d:
            self.map.player.pressed_weapon = False
        elif event.key == pygame.K_h:
            self.map.player.pressed_handel = False
        elif event.key == pygame.K_s:
            self.map.player.pressed_enter_next_level = False
        elif event.key == pygame.K_t:
            self.map.player.pressed_drink = False

    def check_mouse_pressed(self, event):
        if self.pop_up is not None:
            # todo
            if pygame.mouse.get_pressed()[0]:
                self.pop_up.mouse_pressed(event)
                print(f"Possition x ={self.clicked_x} possition y= {self.clicked_y}")

    def check_mouse_released(self, event):
        if self.pop_up != None:
            if event.button:
                pass

    def next_level(self):
        for w in range(self.map.width):
            for h in range(self.map.height):
                self.map.fields[w][h].objects = []
        self.map.enemies = []
        self.map.bats = []
        self.map.spiders = []
        self.map.skeletons = []
        self.map.rocks = []
        self.map.minerals = []
        self.map.MM = []
        self.map.webs = []
        self.map.ladders = []
        self.map.water = []
        self.map.lava = []
        self.map.ladders = []
        player = self.map.get_player()
        player.field = None
        self.map.set_position(player, player.x, player.y)
        # generate level
        self.map.generate_rocks()
        self.level += 1
        self.map.generate_enemies()
        self.map.ladder = Ladder(self)
        field = self.map.get_no_bounadry_field()
        self.map.set_position(self.map.ladder, field.x, field.y)
        self.map.ladders.append(self.map.ladder)
        if self.level % 3 == 1:
            self.map.MysteryMan = MysteryMan(self)
            field2 = self.map.get_no_bounadry_field()
            self.map.set_position(self.map.MysteryMan, field2.x, field2.y)
            self.map.MM.append(self.map.MysteryMan)

    def end_game(self):
        sys.exit()

    def update(self, elapsed):
        self.map.player.update(elapsed)
        self.ran += 1

        if self.ran % 800 == 0:

            for bat in self.map.bats:
                bat.update()
                bat.bat_attack(self.map.player)

            for spiders in self.map.spiders:
                spiders.web_attack(self.map.player, self.map.webs)
            for w in self.map.webs:
                w.update()

            for skeleton in self.map.skeletons:
                skeleton.skeleton_attack(self.map.player)
                skeleton.move_toward_player(self.map.player, self.map)

            for lava in self.map.lava:
                lava.player_on(self.map.player)


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = Game()
    ai.run_game()
