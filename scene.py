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
        self.item_views_used=[]
        self.item_views_shop=[]
        self.item_views_inventory=[]
        self.price_views=[]
        self.pressed_mouse=False
        self.rectangles=[]
        self.left=100
        self.top=200
        self.create_items_to_shop()

        # for i in range(len(self.shopkeeper.goods)):
        #     self.item_views_shop.append(ItemView(self.left+10+(i%5)*50,self.top+10+(i//5)*50,40,40,self.shopkeeper.goods[i]))
        #     # def __init__(self, rect, font, text_color, bg_color, text=''):
        #     self.price_views.append(TextView(pygame.rect.Rect(self.item_views_shop[i].x,self.item_views_shop[i].y+self.item_views_shop[i].h+5,self.item_views_shop[i].w,50),self.game.graphics.font,(0,0,0),(100,100,100),'abc'))

    # rect = pygame.rect.Rect(x_center - 24, y_center - 24, 48, 48)
    # pygame.draw.rect(screen, (220, 127, 100), rect)

    def draw(self):
        pygame.draw.rect(self.game.screen,(100,100,200),self.menuRect)
        pygame.draw.rect(self.game.screen,(100,100,200),self.inventoryRect)
        #na danej pozycji rysuje kwadrat

        for item_view in self.item_views_shop:
            #mini_rect=pygame.rect.Rect(item_view.x+z+self.left+((i+1)%6)*10,item_view.y+self.top+(j)*10,item_view.w,item_view.h)
            pygame.draw.rect(self.game.screen,(20,10,10),item_view.rect)
            #screen.blit(self.game.graphics.emerald_texture, (x_center - 24, y_center - 24))
            self.game.screen.blit(item_view.item.image,(item_view.x+1,item_view.y+1))
        for item_view in self.item_views_inventory:
            pygame.draw.rect(self.game.screen, (20, 10, 10), item_view.rect)
            self.game.screen.blit(item_view.item.image, (item_view.x + 1, item_view.y + 1))
        for item_view in self.item_views_used:
            pygame.draw.rect(self.game.screen, (20, 10, 10), item_view.rect)
            self.game.screen.blit(item_view.item.image, (item_view.x + 1, item_view.y + 1))


        for i in self.price_views:
            i.draw(self.game.screen)

    def mouse_pressed(self,event):
        x,y=pygame.mouse.get_pos()
        #todo
        if pygame.mouse.get_pressed()[0]:
            field_clicked=self.find_clicked_item_view(x,y,self.item_views_shop)
            if field_clicked!=-1:
                self.game.map.player.buy_item(field_clicked)
                self.game.pop_up.create_items_to_shop()
                self.game.map.player.generate_score_image()
            else:
                field_clicked=self.find_clicked_item_view(x,y,self.item_views_inventory)
                if field_clicked!=-1:
                    self.game.map.player.use_item(self.item_views_inventory[field_clicked].item)
                    self.create_items_to_shop()

    def create_items_to_shop(self):
        self.item_views_used=[]
        self.item_views_inventory=[]
        self.item_views_shop=[]
        self.price_views=[]
        for i in range(len(self.shopkeeper.goods)):
            self.item_views_shop.append(ItemView(self.menuRect.x+10+(i%5)*50,self.menuRect.y+10+(i//5)*50,40,40,self.shopkeeper.goods[i]))

            self.price_views.append(TextView(pygame.rect.Rect(self.item_views_shop[i].x,self.item_views_shop[i].y+self.item_views_shop[i].h+5,self.item_views_shop[i].w,50),self.game.graphics.font,(0,0,0),(100,100,100),str(self.shopkeeper.goods[i].price)))
        j=0
        for i in range(len(self.game.map.player.inventory)):
            if self.game.map.player.is_item_used(self.game.map.player.inventory[i])==False:
                self.item_views_inventory.append(ItemView(self.inventoryRect.x + (j % 5) *50+10, self.inventoryRect.y +350 + (j // 5) * 50, 40, 40,self.game.map.player.inventory[i]))
                j+=1

        self.item_views_used.append(ItemView(800,250,40,40,self.game.map.player.current_weapon))
        self.item_views_used.append(ItemView(850, 300, 40, 40, self.game.map.player.current_lantern))
        self.item_views_used.append(ItemView(750, 300, 40, 40, self.game.map.player.current_clothing))
        self.item_views_used.append(ItemView(800, 350, 40, 40, self.game.map.player.current_pickaxe))

    def find_clicked_item_view(self,x,y,list):
        i=0
        for item_view in list:
            if item_view.x <= x and item_view.x + item_view.w >= x and item_view.y <= y and item_view.y + item_view.h >= y:
                return i
            i+=1
        #nie ma itemu
        return -1
