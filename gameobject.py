
class GameObject:

    def __init__(self,game,collectible):
        self.field=None
        self.x=0
        self.y=0
        self.game=game
        self.isCollectible=collectible

    def hit_by_axe(self):
        pass

    def hit_by_weapon(self):
        pass


