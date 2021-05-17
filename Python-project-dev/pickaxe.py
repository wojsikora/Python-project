
from item import Item

class Pickaxe(Item):

    def __init__(self,power,image,price):
        super().__init__(Item.PICKAXE,price)
        self.power=power
        self.image=image
