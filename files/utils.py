import pygame
from files.constants import *

class SpriteSheet():

    frame_count,width,height,scale,colour = 0,0,0,0,0

    def __init__(self,sheet):
        self.sheet = sheet
    
    def return_image(self,frame):
        image = pygame.Surface((self.width,self.height)).convert_alpha()
        image.fill(BLUE)
        image.blit(self.sheet , (0,0) , (frame * self.width , 0 , self.width ,  self.height))
        image = pygame.transform.scale(image , (int(self.scale * self.width) , int(self.scale * self.height)))
        image.set_colorkey(self.colour)

        return image
    
    def return_image_list(self , frames , width , height , scale , colour):

        self.frame_count = frames
        self.width = width
        self.height = height
        self.scale = scale 
        self.colour = colour

        list = []
        
        for i in range(self.frame_count):
            list.append(self.return_image(i))

        return list

def lerp(a,b,t):
    return a + t * (b - a)
