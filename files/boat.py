import pygame
import math
from files.utils import *

class Boat():
    def __init__(self, x, y, dir):

        self.real_pos   = pygame.Vector2(x, y)            #fractional position
        self.int_pos    = pygame.Vector2(x, y)            #integral position
        self.direction  = dir
        self.isMoving   = False
        self.Move       = False

    def update(self, dt):
        if self.Move:
            match self.direction:
                case 0:
                    self.int_pos.y -= 1

                case 1:
                    self.int_pos.x += 1

                case 2:
                    self.int_pos.y += 1

                case 3:
                    self.int_pos.x -= 1
            
            self.isMoving   = True
            self.Move       = False

        if self.isMoving:
            self.real_pos.x = lerp(self.real_pos.x , self.int_pos.x , 3 * dt)
            self.real_pos.y = lerp(self.real_pos.y , self.int_pos.y , 3 * dt)
            if self.real_pos == self.int_pos:
                self.isMoving = False
    
    def shift( self , direction):
        match direction:
            case 0:
                self.int_pos.y -= 1

            case 1:
                self.int_pos.x += 1

            case 2:
                self.int_pos.y += 1

            case 3:
                self.int_pos.x -= 1
        self.isMoving = True

    def unshift(self , direction):
        match direction:
            case 0:
                self.int_pos.y += 1
            
            case 1:
                self.int_pos.x -= 1

            case 2:
                self.int_pos.y -= 1

            case 3:
                self.int_pos.x += 1
        self.isMoving = True