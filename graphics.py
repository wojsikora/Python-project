import pygame


class Graphics():

    def __init__(self):
        picture = pygame.image.load('GUI/images/diamond.png')
        self.diamond_texture = pygame.transform.scale(picture, (48, 48))
        picture2 = pygame.image.load('GUI/images/emerald.png')
        self.emerald_texture = pygame.transform.scale(picture2, (48, 48))
        picture3 = pygame.image.load('GUI/images/gold.png')
        self.gold_texture = pygame.transform.scale(picture3, (48, 48))
        self.font = pygame.font.SysFont(None, 48)
        picture4 = pygame.image.load('GUI/images/bat.png')
        self.bat_texture = pygame.transform.scale(picture4, (48, 48))
        picture5 = pygame.image.load('GUI/images/spider.png')
        self.spider_texture = pygame.transform.scale(picture5, (48, 48))
        picture6 = pygame.image.load('GUI/images/skeleton.png')
        self.skeleton_texture = pygame.transform.scale(picture6, (48, 48))
        picture8 = pygame.image.load('GUI/images/web.png')
        self.web_texture = pygame.transform.scale(picture8, (48, 48))
        cob_pickaxe = pygame.image.load('GUI/images/coblestone_pickaxe.png')
        self.cobelstone_pickaxe = pygame.transform.scale(cob_pickaxe, (35, 35))
        diam_pickaxe = pygame.image.load('GUI/images/pickaxe.jpg')
        self.diamond_pickaxe = pygame.transform.scale(diam_pickaxe, (35, 35))
        gold_pickaxe = pygame.image.load('GUI/images/golden_pickaxe.png')
        self.golden_pickaxe = pygame.transform.scale(gold_pickaxe, (35, 35))
        ir_pickaxe = pygame.image.load('GUI/images/iron_pickaxe.jpg')
        self.iron_pickaxe = pygame.transform.scale(ir_pickaxe, (35, 35))
        picture9 = pygame.image.load('GUI/images/miner.png')
        self.miner_texture = pygame.transform.scale(picture9, (48, 48))
        picture10 = pygame.image.load('GUI/images/copper.png')
        self.copper_texture = pygame.transform.scale(picture10, (48, 48))
        picture11 = pygame.image.load('GUI/images/door.png')
        self.door_texture = pygame.transform.scale(picture11, (48, 48))
        picture12 = pygame.image.load('GUI/images/merchant.png')
        self.merchant_texture = pygame.transform.scale(picture12, (48, 48))
        picture13 = pygame.image.load('GUI/images/box.png')
        self.box_texture = pygame.transform.scale(picture13, (48, 48))
        lantern_1 = pygame.image.load('GUI/images/Torch.gif')
        self.lantern_texture = pygame.transform.scale(lantern_1, (35, 35))
        picture14 = pygame.image.load('GUI/images/bedrocktexture.bmp')
        self.bedrock_texture = pygame.transform.scale(picture14, (48, 48))
        picture15 = pygame.image.load('GUI/images/water.png')
        self.water_texture = pygame.transform.scale(picture15, (48, 48))
        picture16 = pygame.image.load('GUI/images/lava.png')
        self.lava_texture = pygame.transform.scale(picture16, (48, 48))
        picture17 = pygame.image.load('GUI/images/sword.png')
        self.sword_texture = pygame.transform.scale(picture17, (35, 35))
        picture18 = pygame.image.load('GUI/images/armor2.png')
        self.armor1_texture = pygame.transform.scale(picture18, (35, 35))
        picture19 = pygame.image.load('GUI/images/armor1.png')
        self.armor2_texture = pygame.transform.scale(picture19, (35, 35))
