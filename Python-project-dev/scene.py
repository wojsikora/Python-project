import pygame
from item_view import ItemView
from text_view import TextView
class ShopScene:

    def __init__(self,game,shopkeeper):
        self.game=game
        self.menuRect=pygame.Rect(100,200,400,400)
        self.inventoryRect=pygame.Rect(650,200,400,400)
        self.listOfItems=[None]*10
        self.shopkeeper=shopkeeper
        self.item_views=[]
        self.price_views=[]
        self.pressed_mouse=False
        self.rectangles=[]
        self.left=100
        self.top=200
        for i in range(len(self.shopkeeper.goods)):
            self.item_views.append(ItemView(self.left+10+(i%5)*50,self.top+10+(i//5)*50,40,40,self.shopkeeper.goods[i]))
            # def __init__(self, rect, font, text_color, bg_color, text=''):
            self.price_views.append(TextView(pygame.rect.Rect(self.item_views[i].x,self.item_views[i].y+self.item_views[i].h+5,self.item_views[i].w,50),self.game.graphics.font,(0,0,0),(100,100,100),'abc'))

    # rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
    # pygame.draw.rect(screen, (220, 127, 100), rect)
    def draw(self):
        pygame.draw.rect(self.game.screen,(100,100,200),self.menuRect)
        pygame.draw.rect(self.game.screen,(100,100,200),self.inventoryRect)
        #na danej pozycji rysuje kwadrat
        i=0
        for item_view in self.item_views:

            #mini_rect=pygame.rect.Rect(item_view.x+z+self.left+((i+1)%6)*10,item_view.y+self.top+(j)*10,item_view.w,item_view.h)
            pygame.draw.rect(self.game.screen,(20,10,10),item_view.rect)

            #screen.blit(self.game.graphics.emerald_texture, (x_center - 24, y_center - 24))
            if i<5:
                self.game.screen.blit(self.shopkeeper.goods[i].image,(item_view.x+1,item_view.y+1))
            i+=1
        for i in self.price_views:
            i.draw(self.game.screen)
    def mouse_pressed(self,event):
        x,y=pygame.mouse.get_pos()
        #todo
        if pygame.mouse.get_pressed()[0]:
            nr=1
            for item_view in self.item_views:
                if item_view.x<=x and item_view.x+item_view.w>=x and item_view.y<=y and item_view.y+item_view.h>=y:
                    print(f"The rectangle number {nr} was clicked")
                nr+=1
                self.pressed_mouse==False


    def buy(self):
        pass

    def create(self):
        pass