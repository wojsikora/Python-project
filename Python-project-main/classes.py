from gameobject import GameObject
from mineral import Mineral
import pygame
from mysteryman import MysteryMan
from scene import ShopScene
import math

class Player(GameObject):
    # GOLD = 0
    # COPPER = 1
    # EMERALD = 2
    # DIAMOND = 3
    # BEDROCK = 4
    def __init__(self,game,health,gas):
        super().__init__(game,False)
        self.gas=gas #paliwo
        self.health=health
        self.crystals_count=0
        self.crystals=[0]*5
        self.inventory=[]
        self.generate_score_image()
        #jednostki w okreslonym czasie //1sekunda
        self.velocity_x=0
        self.velocity_y=0
        #aby niszczyc skały kilof
        self.pressed_axe=False
        #aby walczyc w przeciwnikami
        self.pressed_weapon = False
        #do handlu
        self.pressed_handel=False

    def increment_mineral(self,mineral_type):
        self.crystals[mineral_type]+=1
        self.generate_score_image()
        
    def draw(self,screen,x_center,y_center):

        rect=pygame.rect.Rect(x_center-10,y_center-10,20,20)

        pygame.draw.rect(screen,(255,0,0),rect)
        #screen.blit(self.game.graphics.diamond_texture, (x_center - 24, y_center - 24))
        screen.blit(self.scores_image,(0,0))
        screen.blit(self.health_image,(1040,0))
    #elapsed w milisekundach
    #przemieszczanie

    def update(self,elapsed):
        if self.health<=0:
            print("NO HP")
            sys.exit()

        if self.pressed_axe==True or self.pressed_weapon==True:
            #prawo
            if self.velocity_x>0:
                offset_x=1
            elif self.velocity_x<0:
                offset_x=-1
            else:
                offset_x=0

            if self.velocity_y>0:
                offset_y=1
            elif self.velocity_y<0:
                offset_y=-1
            else:
                offset_y=0
            #print("hiawfd")
            if offset_x!=0 or offset_y!=0:
                #wspólrzedne gracza
                field_x=self.field.x+offset_x
                field_y=self.field.y+offset_y
                #wyjscie za mape
                if field_x>=0 and field_x<self.game.map.width and field_y>=0 and field_y<self.game.map.height:
                    for obj in self.game.map.fields[field_x][field_y].objects:
                        print("hit")
                        if self.pressed_axe==True:
                            obj.hit_by_axe()
                        elif self.pressed_weapon==True:
                            obj.hit_by_weapon()
        elif self.pressed_handel==True:
            for i in range(3):
                for j in range(3):
                    #wyliczam pozycje
                    x_position=int(self.x+i-1)
                    y_position=int(self.y+j-1)
                    if self.x==x_position or self.y==y_position:
                        continue
                    for obj in self.game.map.fields[x_position][y_position].objects:
                        if(isinstance(obj,MysteryMan)):
                           self.game.pop_up=ShopScene(self.game,obj)
        else:
            p_x=int(self.x+self.velocity_x*elapsed/1000)
            p_y=int(self.y+self.velocity_y*elapsed/1000)
            #nie wychodzi pozaplansze
            if p_x<0:
                p_x=0
            elif p_x>=self.game.map.width:
                p_x=self.game.map.width-1
            if p_y<0:
                p_y=0
            elif p_y>=self.game.map.height:
                p_y=self.game.map.height-1

            for obj in self.game.map.fields[p_x][p_y].objects:
                if self is obj:
                    continue
                if obj.isCollectible==False:
                    return
            self.game.map.set_position(self,self.x+self.velocity_x*elapsed/1000,self.y+self.velocity_y*elapsed/1000)
            self.collect_collectibles()
            self.generate_health_image()

    def destroy_rocks(self,x,y):

        for obj in self.game.map.fields[x][y].objects:

            if obj.isCollectible==False:
                pass

    def collect_collectibles(self):

        for obj in self.field.objects:
            if isinstance(obj,Mineral):
                self.crystals_count+=1
                self.increment_mineral(obj.mineral_type)
                self.game.map.remove_game_object(obj)
                break

    def generate_score_image(self):
        string =''
        for i in self.crystals:
            if len(string) > 0:
                string += ','
            string += str(i)
        self.scores_image=self.game.graphics.font.render(string,True,(255,0,0),(0,0,255))

    def generate_health_image(self):
        string = 'health: '
        string += str(self.health)
        self.health_image=self.game.graphics.font.render(string, True, (255,0,0), (0,0,255))
