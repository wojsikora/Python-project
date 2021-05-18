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
        # self.rock=Rock(game,1,screen,True)
        self.nr_destructible_obj=destructable_obj
        self.nr_indestructible_obj=indestructable_obj
        self.width=width
        self.height=height
        self.stones_number = int(width*height/4)
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



    def check_if_in_map(self, x, y, a, b):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        if x + dx[a] >= 0 and x + dx[a] < self.width and y + dy[b] >= 0 and y + dy[b] < self.height and self.check_if_taken(x + dx[a], y + dy[b] ):
            return (x + dx[a], y + dy[b])
        else:
            return None

    def generate_surrounding_stones(self, x, y):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        num = random.randint(2,5)


        for i in range(num):
            a = random.randint(0, 7)
            b = random.randint(0, 7)

            while(self.check_if_in_map(x, y, a, b) == None):
                a = random.randint(0, 7)
                b = random.randint(0, 7)

            stone = Rock(self.game, 1, self.screen, False)
            self.set_position(stone, x + dx[a] + 0.5, y + dy[b]+ 0.5)
            self.rocks.append(stone)










    def generate_rocks(self):
        nr_obj=0
        while(nr_obj<self.nr_destructible_obj):
            # x1=random.randint(0,self.width-1)
            # y1=random.randint(0,self.height-1)
            f=self.get_random_field()
            rock1 = Rock(self.game,1, self.screen,True)
            self.set_position(rock1,f.x+0.5,f.y+0.5)
            nr_obj=nr_obj+1
            self.rocks.append(rock1)
            self.generate_surrounding_stones(f.x, f.y)
        nr_obj3=0
        #while(nr_obj3<self.nr_destructible_obj):
        while (nr_obj3 < self.stones_number):
            # x1 = random.randint(0, self.width - 1)
            # y1 = random.randint(0, self.height - 1)
            f = self.get_random_field()
            rock1 = Rock(self.game, 1, self.screen, False)
            self.set_position(rock1, f.x + 0.5, f.y + 0.5)
            nr_obj3 = nr_obj3 + 1
            self.rocks.append(rock1)
        nr_obj2=0
        while(nr_obj2<self.nr_indestructible_obj):
            # x2= random.randint(0, self.width - 1)
            # y2= random.randint(0, self.height - 1)
            f=self.get_random_field()
            if len(self.fields[f.x][f.y].objects)==0:
                #srodek pola
                rock2 = Rock(0)
                self.set_position(rock2,f.x+0.5,f.y+0.5)
                nr_obj2=nr_obj2+1
                self.rocks.append(rock2)

    def generate_enemies(self):
        bats,skeletons,spiders=self.game.lvl_info.enemy_quantities[self.game.level]
        for b in range(bats):
            f=self.get_random_field()
            self.bat=Bat(self.game,5,5)
            self.bat.enemy_type=0
            self.set_position(self.bat,f.x,f.y)
            self.bats.append(self.bat)
           # self.enemies.append(bat)
        for s in range(skeletons):
            f=self.get_random_field()
            #self.skeleton=Skeleton()
            #self.skeleton.enemy_type=2
            #self.set_position(self.skeleton_,f.x,f.y)
            #self.skeletons.append(self.skeleton_)
            self.enemy3 = Enemy(self.game, 100, 10)
            self.enemy3.enemy_type = 2
            self.set_position(self.enemy3, f.x, f.y)
            self.enemies.append(self.enemy3)
            #self.enemies(skeleton_)
        for sp in range(spiders):
            f=self.get_random_field()
            self.spider=Spider(self.game,10,10)
            self.spider.enemy_type=1
            self.set_position(self.spider,f.x,f.y)
            self.spiders.append(self.spider)
            #self.enemies.append(spidey)

    def add_mineral(self,mineral):
            self.minerals.append(mineral)


    def get_random_field(self):
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            if self.check_if_taken(pos_x, pos_y):
                return self.fields[pos_x][pos_y]

    def check_if_taken(self, x, y):
        if len(self.fields[x][y].objects) == 0:
            return True
        return False
