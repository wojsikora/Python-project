from field import Field
import classes
from rock import Rock
import random
from enemy import Enemy
from mineral import Mineral
from mysteryman import MysteryMan
from bat import Bat
from spider import Spider
from skeleton import Skeleton
from web import Web
import cmath
from leader import Leader

class Map:

    def __init__(self,game,width,height,destructable_obj,indestructable_obj,screen):
        self.player=classes.Player(game,50, 10)
        self.MysteryMan=MysteryMan(game)
        self.screen=screen
        self.game=game
        self.leader = Leader(self.game)
        #self.Web = Web(self.game, 0, 0)
        self.rock=Rock(game,1,screen)
        self.nr_destructible_obj=destructable_obj
        self.nr_indestructible_obj=indestructable_obj
        self.width=width
        self.height=height
        self.enemies=[]
        self.bats=[]
        self.spiders = []
        self.skeletons = []
        self.fields=[None]*width
        self.rocks=[]
        self.minerals=[]
        self.MM=[]
        self.webs=[]
        self.leaders=[]
        #wypelniam tablice
        for x in range(0,width):
            self.fields[x]=[None]*height
            for y in range(0,height):
                self.fields[x][y]=Field(x, y)
        self.set_position(self.MysteryMan,5.5,5.5)
        self.set_position(self.player,0.5,0.5)
        #self.set_position(self.rock,1.5,2.5)
        self.bat=Bat(game, 5, 5)
        self.bat.enemy_type = 0
        self.spider = Spider(game, 10, 10)
        self.spider.enemy_type = 1
        #self.enemy2 = Enemy(game, 100, 10)
        #self.enemy2.enemy_type = 1
        self.enemy3 = Enemy(game, 100, 10)
        self.enemy3.enemy_type = 2
        self.set_position(self.bat,6,6)
        self.set_position(self.spider, 12, 12)
        #self.set_position(self.enemy2, 12, 12)
        self.set_position(self.enemy3, 8, 8)
        #self.enemies.append(self.enemy)
        self.bats.append(self.bat)
        self.spiders.append(self.spider)
        #self.enemies.append(self.enemy2)
        self.enemies.append(self.enemy3)
        self.MM.append(self.MysteryMan)
        field=self.get_random_field()
        self.set_position(self.leader,field.x,field.y)
        self.leaders.append(self.leader)
        #self.webs.append(self.Web)
        #self.set_position(self.Web, 9, 9)


    def set_position(self,game_object,x,y):
        field_x=int(x)
        field_y=int(y)
        new_field=self.fields[field_x][field_y]
        if game_object.field==None:
            game_object.field=new_field
            new_field.objects.append(game_object)
        elif new_field is not game_object.field:
            game_object.field.objects.remove(game_object)
            game_object.field = new_field
            new_field.objects.append(game_object)
        # if game_object.field!=None:
        #     game_object.field.object_at_field=None
        # #ustawiam na pozycji
        # game_object.field=field
        # if field!=None:
        #     #teraz tam jest gameobject
        #     field.object=game_object
        game_object.x=x
        game_object.y=y


    def get_player(self):
        return self.player

    def remove_game_object(self,object):

        object.field.objects.remove(object)
        if isinstance(object,Rock):
            self.rocks.remove(object)
        elif isinstance(object,Enemy):
            if isinstance(object, Bat):
                self.bats.remove(object)
            elif isinstance(object, Spider):
                self.spiders.remove(object)
            else:

                self.enemies.remove(object)
        elif isinstance(object,Mineral):
            self.minerals.remove(object)
        elif isinstance(object, Web):
            self.webs.remove(object)


    def generate_rocks(self):
        nr_obj=0
        while(nr_obj<self.nr_destructible_obj):
            x1=random.randint(0,self.width-1)
            y1=random.randint(0,self.height-1)
            field1=Field(x1,y1)
            if len(self.fields[x1][y1].objects)==0:
                rock1 = Rock(self.game,1, self.screen)
                self.set_position(rock1,x1+0.5,y1+0.5)
                nr_obj=nr_obj+1
                self.rocks.append(rock1)
        nr_obj2=0

        while(nr_obj2<self.nr_indestructible_obj):
            x2= random.randint(0, self.width - 1)
            y2= random.randint(0, self.height - 1)
            field2 = Field(x2, y2)
            if len(self.fields[x1][y1].objects)==0:
                #srodek pola
                rock2 = Rock(0)
                self.set_position(rock2,x2+0.5,y2+0.5)
                nr_obj2=nr_obj2+1
                self.rocks.append(rock2)
    def add_mineral(self,mineral):
        self.minerals.append(mineral)

    def get_random_field(self):
        pos_x=random.randint(0,self.width-1)
        pos_y=random.randint(0,self.height-1)
        if len(self.fields[pos_x][pos_y].objects)==0:
            return self.fields[pos_x][pos_y]
