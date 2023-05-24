import sys
import pygame as pyg
from pygame.locals import *
import random as rndm
import PIL.Image 


(width,height) = (480,480)

#SET Color Tuple
WHITE = (255,255,255)
BLUE = (0,0,255)
LIGHT_PINK = (255,152,215)
LIGHT_SKYBLUE =(184,255,248)
BLACK = (0,0,0)

#4 Convinience 
#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
class SpriteDimension:
    def __init__(self, sprite_name):
        self.width, self.height = PIL.Image.open(sprite_name).size

class TextFont_Display :
    class ComicSans():
        color = (BLACK,WHITE)
        def __init__(self, your_text, size, coords,colorOfTextnBG):
            self.color = colorOfTextnBG
            thisfont = pyg.font.Font('fonts/ComicSans.ttf', 32)
            #render(text, antialias, color, background=None)
            self.RenText = thisfont.render(your_text, True, self.color[0] , self.color[1])
            self.textRect = self.RenText.get_rect()
            self.textRect.center = coords
#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆
#4 Convinence 

referingtoBobBBPX_Fruits_List = []
def refertoBobBBPX_Fruits_List(value):
    referingtoBobBBPX_Fruits_List = value



#Characters
class LunaPX:
    spriteimg_dir= "assets/LunaPX_sprite.png"


    #set coords to random spot in player ground
    xpos = (width,height)[0]/2 - 45/2
    ypos = height//2+height//4

    #Scoring
    class Scoring:
        Misses = 0
        Catches = 0
        Stolen = 0
    def __init__(self, displayOnWindow) -> None:
        #set what Window to display this into
        self.DISPLAY = displayOnWindow
    def draw(self):

        #Loading sprite...
        self.Load = pyg.image.load(self.spriteimg_dir)
        #...into window
        self.DISPLAY.blit(self.Load, (self.xpos,self.ypos))
    
    def update(self):
        #controls a=left d=right
        keys_press = pyg.key.get_pressed()
        
        if keys_press[pyg.K_a]:
            self.xpos -= 1
        
        if keys_press[pyg.K_d]:
            self.xpos += 1
        

class LunantPX:
    spriteimg_dir= "assets/LunantPX_sprite.png"


    #set coords to random spot in player ground
    xpos = rndm.randint(0, width)
    ypos = height//2+height//4

    class Scoring:
        Misses = 0
        Catches = 0
        Stolen =0

    def __init__(self, displayOnWindow) -> None:
        #set what Window to display this on
        self.DISPLAY = displayOnWindow
        self.DISPLAY = displayOnWindow
    def draw(self):

        #Loading sprite..
        self.Load = pyg.image.load(self.spriteimg_dir)
        #..into window
        self.DISPLAY.blit(self.Load, (self.xpos,self.ypos))
    
    def update(self):
        #controls j=left l=right
        keys_press = pyg.key.get_pressed()
        
        if keys_press[pyg.K_j]:
            self.xpos -= 1
        if keys_press[pyg.K_l]:
            self.xpos += 1


#Add Characters
class addBobBBPX_Fruit:
    spriteimg_dir= "assets/BobBBPX_sprite.png"



    ypos = -1*SpriteDimension(spriteimg_dir).height
    

    
    def __init__(self,displayOnWindow,xpos=None):
        #set what Window to display this on
        self.DISPLAY = displayOnWindow
        self.xpos = xpos if xpos != None else rndm.randint(0, width)



    def draw(self):
        self.Load = pyg.image.load(self.spriteimg_dir)
        self.DISPLAY.blit(self.Load, (self.xpos,self.ypos))
    def update(self, HomeList, Actual_LunaPX, Actual_LunantPX):
        self.HomeList = HomeList
        self.ypos += 0.5

        #if i reach bottom
        if self.ypos > height:
            # Remove the fruit from the Fruits list/Make fruit disapear
            HomeList.remove(self)

            #Luna and Lunant Both miss
            LunaPX.Scoring.Misses += 1
            LunantPX.Scoring.Misses +=1

        #if Luna collition w/ BobBBPX
        if Actual_LunaPX.xpos + SpriteDimension(Actual_LunaPX.spriteimg_dir).width > self.xpos and Actual_LunaPX.xpos < self.xpos + SpriteDimension(self.spriteimg_dir).width and Actual_LunaPX.ypos + SpriteDimension(Actual_LunaPX.spriteimg_dir).height > self.ypos and Actual_LunaPX.ypos < self.ypos + SpriteDimension(self.spriteimg_dir).height:
            
            if Actual_LunantPX.xpos + SpriteDimension(Actual_LunantPX.spriteimg_dir).width > self.xpos and Actual_LunantPX.xpos < self.xpos + SpriteDimension(self.spriteimg_dir).width and Actual_LunantPX.ypos + SpriteDimension(Actual_LunantPX.spriteimg_dir).height > self.ypos and Actual_LunantPX.ypos < self.ypos + SpriteDimension(self.spriteimg_dir).height:
                HomeList.remove(self)
                LunaPX.Scoring.Catches += 1
                LunantPX.Scoring.Catches += 1
            else:
                # Remove the fruit from the Fruits list/Make fruit disapear
                HomeList.remove(self)

                LunaPX.Scoring.Catches += 1
                LunantPX.Scoring.Stolen +=  1
        #if Lunant collision w/ BobBBPX
        elif Actual_LunantPX.xpos + SpriteDimension(Actual_LunantPX.spriteimg_dir).width > self.xpos and Actual_LunantPX.xpos < self.xpos + SpriteDimension(self.spriteimg_dir).width and Actual_LunantPX.ypos + SpriteDimension(Actual_LunantPX.spriteimg_dir).height > self.ypos and Actual_LunantPX.ypos < self.ypos + SpriteDimension(self.spriteimg_dir).height:
            # Remove the enemy from the enemies list
            HomeList.remove(self)

            LunantPX.Scoring.Catches += 1
            LunaPX.Scoring.Stolen +=  1

        if HomeList ==[]:
        
           addNew_addBobBBPX_Fruit(1, self.HomeList, self.DISPLAY)

            
           
            
class addFruit:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, spriteimg_dir, window_display):
        self.sprite = spriteimg_dir
        self.window_display = window_display
        self.SpriteLoad = pyg.image.load(spriteimg_dir)
        self.window_display.blit(self.SpriteLoad, (self.xpos,self.ypos))



def addNew_addBobBBPX_Fruit(howmuch_new, HomeList, displayOnWindow):
    for i in range(howmuch_new):
        HomeList.append(addBobBBPX_Fruit(displayOnWindow))



def main():
    

    pyg.init()
    
    
    DISPLAY = pyg.display.set_mode((width,height))
    pyg.display.set_caption("Epic Game")
    
    #setup character instances
    The_LunaPX = LunaPX(DISPLAY)
    The_LunantPX = LunantPX(DISPLAY)

    BobBBPX_Fruits_List = [addBobBBPX_Fruit(DISPLAY)]
    
    refertoBobBBPX_Fruits_List(BobBBPX_Fruits_List)
    while True:
        The_LunaPX_ScoreText = TextFont_Display.ComicSans(f"Catches: {The_LunaPX.Scoring.Catches} Misses: {The_LunaPX.Scoring.Misses} Stolen: {The_LunaPX.Scoring.Stolen}",8, (height//2,22), (BLACK, LIGHT_PINK))
        The_LunantPX_ScoreText = TextFont_Display.ComicSans(f"Catches: {The_LunantPX.Scoring.Catches} Misses: {The_LunantPX.Scoring.Misses} Stolen: {The_LunantPX.Scoring.Stolen}",8, (height//2,22*3), (BLACK,LIGHT_SKYBLUE))
        #Close Button
        for event in pyg.event.get():
            if event.type ==QUIT:
                pyg.quit()
                sys.exit()

        
        #"Diplay stuff on the Window" code 
        #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
        
        DISPLAY.fill(WHITE)
        DISPLAY.blit(The_LunaPX_ScoreText.RenText, The_LunaPX_ScoreText.textRect)
        DISPLAY.blit(The_LunantPX_ScoreText.RenText, The_LunantPX_ScoreText.textRect)
        
        The_LunaPX.draw()
        The_LunantPX.draw()

        
            
        for BobBBPX_Fruit in BobBBPX_Fruits_List:
            BobBBPX_Fruit.draw()
            BobBBPX_Fruit.update(BobBBPX_Fruits_List,The_LunaPX,The_LunantPX)
        
        The_LunaPX.update()
        The_LunantPX.update()
        pyg.display.update()
        #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆
        #"Diplay stuff on the Window" code 
main()
