import sys
import pygame as pyg
from pygame.locals import *
import random as rndm
import PIL.Image 


(width,height) = (480,480)

#Sprite dir
LunaPX = "assets/LunaPX_sprite.png"
LunantPX = "assets/LunantPX_sprite.png"
BobBBPX = "assets/Bob-bonbonPX_sprite.png"


#SET Color Tuple
WHITE = (255,255,255)
BLUE = (0,0,255)
LIGHT_PINK = (255,152,215)
BLACK = (0,0,0)


class SpriteDimension:
    def __init__(self, sprite_name):
        self.width, self.height = PIL.Image.open(sprite_name).size

class Font:
    class ComicSans():
        def __init__(self, your_text, size, coords):
            thisfont = pyg.font.Font('fonts/ComicSans.ttf', 32)
            #render(text, antialias, color, background=None)
            self.RenText = thisfont.render(your_text, True, BLACK , LIGHT_PINK)
            self.textRect = self.RenText.get_rect()
            self.textRect.center = coords

class StoreScore:
    Catches = 0
    Misses = 0


def resetSpritePos():
    LunaPX_xpos = (width,height)[0]/2 - 45/2
    LunaPX_ypos = (width,height)[1]/2 - 43/2

    Lunant_xpos = rndm.randint(0, width)
    Lunant_ypos = rndm.randint(0, height)

    BobBB_xpos = rndm.randint(0, width)
    BobBB_ypos = -25

class addBobBBPX_Fruit:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, window_display):
        self.window_display = window_display
        BobBBPXLoad = pyg.image.load(BobBBPX)
        self.window_display.blit(BobBBPXLoad, (self.xpos,self.ypos))
    def update(self, HomeList):
        self.ypos += .05
        if self.ypos > height:
            # Remove the enemy from the enemies list
            HomeList.remove(self)

            player_score += 1 

        
        
        
        
        #AAAAAAAAAAAAAAAAAAAAAAAaaaa 
class addFruit:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, spriteimg_dir, window_display):
        self.sprite = spriteimg_dir
        self.window_display = window_display
        self.SpriteLoad = pyg.image.load(spriteimg_dir)
        self.window_display.blit(self.SpriteLoad, (self.xpos,self.ypos))

def main():
    pyg.init()
    
    
    DISPLAY = pyg.display.set_mode((width,height))
    pyg.display.set_caption("Epic Game")
    


    LunaLoad = pyg.image.load("assets/Luna.png")
    LunaPXLoad = pyg.image.load(LunaPX)
    LunantPXLoad = pyg.image.load(LunantPX)
    
    


    LunaPX_xpos = (width,height)[0]/2 - 45/2
    LunaPX_ypos = (width,height)[1]/2 - 43/2

    Lunant_xpos = rndm.randint(0, width)
    Lunant_ypos = rndm.randint(0, height)

    BobBB_xpos = rndm.randint(0, width)
    BobBB_ypos = -25
    
    
    resetSpritePos()
    print("LunaPX: ", LunaPX_xpos,LunaPX_ypos)
    print("Lunan'tPX: ", Lunant_xpos,Lunant_ypos)
    print("BobBBPX: ", BobBB_xpos,BobBB_ypos)

    LunaPX_Score = StoreScore
    LunantPX_Score = StoreScore

    BobBBPX_Fruits_List = [addBobBBPX_Fruit(rndm.randint(0, width),  -abs(SpriteDimension(BobBBPX).height))]
    while True:
        LunaPX_Score_Text = Font.ComicSans(f"Catches: {LunaPX_Score.Catches}\nMisses: {LunaPX_Score.Misses}",13, (2,2))

        for event in pyg.event.get():
            if event.type ==QUIT:
                pyg.quit()
                sys.exit()

        
        #vvvvvvvvvvvvvvvvvvv
        #Luna_ypos= Luna_ypos +0.1
        keys_press = pyg.key.get_pressed()
        if keys_press[pyg.K_w]:
            LunaPX_ypos -= 1
        if keys_press[pyg.K_a]:
            LunaPX_xpos -= 1
        if keys_press[pyg.K_s]:
            LunaPX_ypos += 1
        if keys_press[pyg.K_d]:
            LunaPX_xpos += 1

        if keys_press[pyg.K_i]:
            Lunant_ypos -= 1
        if keys_press[pyg.K_j]:
            Lunant_xpos -= 1
        if keys_press[pyg.K_k]:
            Lunant_ypos += 1
        if keys_press[pyg.K_l]:
            Lunant_xpos += 1
        
        DISPLAY.fill(WHITE)
        DISPLAY.blit(LunaPXLoad, (LunaPX_xpos,LunaPX_ypos))
        DISPLAY.blit(LunantPXLoad, (Lunant_xpos,Lunant_ypos))
        DISPLAY.blit(LunaPX_Score_Text.RenText, LunaPX_Score_Text.textRect)
        BobBB_ypos += .20

        
            
        
        
            
        for BobBBPX_Fruit in BobBBPX_Fruits_List:
            BobBBPX_Fruit.draw(DISPLAY)
            BobBBPX_Fruit.update(BobBBPX_Fruits_List)

        pyg.display.update()
main()
