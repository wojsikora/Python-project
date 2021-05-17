
from item import Item

class Pickaxe(Item):

    def __init__(self,power,image):
        super().__init__(Item.PICKAXE)
        self.power=power
        self.image=image