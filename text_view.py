
def generate_score_image(self):
    string =''
    for i in self.crystals:
        if len(string) > 0:
            string += ','
        string += str(i)
    self.scores_image = self.game.graphics.font.render(string, True, (255, 0, 0), (0, 0, 255))

class TextView():
    def __init__(self,rect,font,text_color,bg_color,text=''):
        self.rect=rect
        self.text_color=text_color
        self.bg_color=bg_color
        self.text=text
        self.font=font
        self.text_image=None


    def set_text(self,text):
        self.text=text
        self.text_image=None

        # self.text_image=self.font.render(self.text,True,self.text_color,self.bg_color)

    def draw(self,screen):

        if self.text_image==None:
            self.text_image = self.font.render(self.text, True, self.text_color, self.bg_color)
        width=self.text_image.get_width()
        height=self.text_image.get_height()
        left=self.rect.x+self.rect.width/2-width/2
        top=self.rect.y+self.rect.height/2-height/2
        screen.blit(self.text_image,(left,top))