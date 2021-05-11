import pygame
from map import Map
from graphics import Graphics
import sys



class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Miner")
        self.graphics = Graphics()
        self.map=Map(self,25,25,5,0,self.screen)
        self.ran=0
        self.pop_up=None
        self.clicked_x=None
        self.cliked_y=None
        #self.player = self.map.player
        #self.camera = Camera(self.player)
        #self.follow = Follow(self.camera, self.player)
        #self.border = Border(self.camera, self.player)
        #self.auto = Auto(self.camera, self.player)
        #self.camera.setmethod(self.follow)


    def run_game(self):
        self.map.generate_rocks()

        while True:
        # Oczekiwanie na nacisniecie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self.check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup(event)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:


            self.update(14)
            self._update_screen()
            #self.camera.scroll()

    def _update_screen(self):

        self.screen.fill((200,200,200))

        # for x in range(self.map.width):
        #
        #     for y in range(self.map.height):
        #
        #         field=self.map.fields[x][y]
        #         rect=pygame.rect.Rect(field.x*50+1,field.y*50+1,48,48)
        #         pygame.draw.rect(self.screen,(100,100,100),rect)
        #         if field.object_at_field!=None:
        #             #podaje srodki
        #             field.object_at_field.draw(self.screen,field.x*50+25,field.y*50+25)
        if self.pop_up==None:
            for rock in self.map.rocks:
                #wymiar w pikselach
                rock.draw(self.screen,rock.x*50,rock.y*50)
            for bat in self.map.bats:
                bat.draw(self.screen, bat.x*50, bat.y*50)
            for spider in self.map.spiders:
                spider.draw(self.screen, spider.x*50, spider.y*50)
            for enemy in self.map.enemies:
                enemy.draw(self.screen,enemy.x*50,enemy.y*50)
            self.map.player.draw(self.screen,self.map.player.x*50,self.map.player.y*50)
            for mineral in self.map.minerals:
                mineral.draw(self.screen,mineral.x*50,mineral.y*50)
            for m in self.map.MM:
               m.draw(self.screen,m.x*50,m.y*50)
            for w in self.map.webs:
                w.draw(self.screen, w.x*50, w.y*50)
        else:
            self.pop_up.draw()

        pygame.display.flip()

    def check_keydown(self,event):
        player=self.map.get_player()
        if event.key==pygame.K_LEFT:
            #self.map.set_position(player, player.x-1,player.y)
            player.velocity_x=-1
        elif event.key==pygame.K_RIGHT:
            #self.map.set_position(player, player.x+1, player.y)
            player.velocity_x=1
        elif event.key==pygame.K_DOWN:
            #self.map.set_position(player,  player.x,player.y+1)
            player.velocity_y=1
        elif event.key==pygame.K_UP:
            #self.map.set_position(player,player.x,player.y-1)
            player.velocity_y=-1
        elif event.key==pygame.K_a:
            self.map.player.pressed_axe=True
        elif event.key==pygame.K_d:
            self.map.player.pressed_weapon=True
        elif event.key==pygame.K_h:
            self.map.player.pressed_handel=True

        #elif event.type == pygame.KEYUP:
         #   self.check_keyup(event)
        #elif event.key == pygame.K_1:
        #    camera.setmethod(follow)
        #elif event.key == pygame.K_2:
         #   camera.setmethod(auto)
        #elif event.key == pygame.K_3:
        #    camera.setmethod(border)
        #camera.scroll()


    def check_keyup(self,event):
        player = self.map.get_player()
        if event.key == pygame.K_LEFT:
            player.velocity_x=0
        elif event.key == pygame.K_RIGHT:
            player.velocity_x=0
        elif event.key == pygame.K_DOWN:
            player.velocity_y = 0
        elif event.key == pygame.K_UP:
            player.velocity_y =0
        elif event.key==pygame.K_a:
            self.map.player.pressed_axe = False
        elif event.key==pygame.K_d:
            self.map.player.pressed_weapon = False
        elif event.key==pygame.K_h:
            self.map.player.pressed_handel=False


    def update(self,elapsed):
        self.map.player.update(elapsed)
        self.ran+=1


        if self.ran % 800 == 0:
            #for e in self.map.enemies:
            if self.map.bat in self.map.bats:
                self.map.bat.update()
                self.map.bat.bat_attack(self.map.player)

            if self.map.spider in self.map.spiders:
                #self.map.enemy2.move_toward_player(self.map.player, self.map)
                self.map.spider.web_attack(self.map.player, self.map.webs)
                for w in self.map.webs:
                    w.update()
                    w.check_if_at_player_position(self.map.player)
            if self.map.spider not in self.map.spiders:
                for w in self.map.webs:
                    w.update()
                    w.check_if_at_player_position(self.map.player)

            if self.map.enemy3 in self.map.enemies:
                self.map.enemy3.skeleton_attack(self.map.player)
                self.map.enemy3.move_toward_player(self.map.player, self.map)





if __name__ == '__main__':
# Utworzenie egzemplarza gry i jej uruchomienie.
    ai = Game()
    ai.run_game()
