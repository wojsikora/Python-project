import random

class Level_Information():

    def __init__(self):
        self.bats_num = 1
        self.skeletons_num = 1
        self.spiders_num = 1
        self.enemy_quantities=[]
        self.enemy_quantities.append((1,1,1))

    def random_num(self):
        r = random.randint(0, 2)
        if r == 0:
            self.bats_num += 1
        elif r == 1:
            self.skeletons_num += 1
        else:
            self.spiders_num += 1

    def generate_new_level(self):
        self.random_num()
        self.enemy_quantities.append((self.bats_num, self.spiders_num, self.spiders_num))