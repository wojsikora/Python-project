import pygame
from item_view import ItemView
class ShopScene:

    def __init__(self,game,shopkeeper):
        self.game=game
        self.menuRect=pygame.Rect(100,200,400,400)
        self.listOfItems=[None]*10
        self.shopkeeper=shopkeeper
        self.item_views=[]
        self.pressed_mouse=False
        for i in range(10):
            self.item_views.append(ItemView(10+(i%5)*40,10+(i//5)*40,40,40,self.shopkeeper.goods[i]))

    # rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
    # pygame.draw.rect(screen, (220, 127, 100), rect)
    def draw(self):
        pygame.draw.rect(self.game.screen,(100,100,200),self.menuRect)
        #na danej pozycji rysuje kwadrat
        i=0
        j=0
        z=0
        for item_view in self.item_views:

            if i%5==0 and i!=0:
                j=j+1
            if i>=5:
                z=10
            mini_rect=pygame.rect.Rect(item_view.x+z+100+((i+1)%6)*10,item_view.y+200+(j)*10,item_view.w,item_view.h)
            pygame.draw.rect(self.game.screen,(20,10,10),mini_rect)
            # rect = pygame.rect.Rect(x_center-24,y_center - 24,48,48)
            # pygame.draw.rect(screen, (255, 233,0),rect)
            i=i+1

    def check_clicked_field(self,x,y):

            for item_view in self.item_views:
