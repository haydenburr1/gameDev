import pygame as pg
from settings import *
import math
import sys

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        # Initialize parameters
        self.theta = 0
        self.radius = 200 # pixels
        self.speed = 0.05
        self.speed_multiplier = 0.1

        self.gravity = 0
        
        # Load the image and set the rect
        self.img = pg.image.load("assets/plane.png").convert_alpha()
        self.rect = self.img.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
    
    def draw(self, screen):
        screen.blit(pg.transform.rotate(self.img, math.degrees(self.theta)), self.rect)
        self.movement()
        self.controls()
    
    def movement(self):
        # Update the position based on theta and radius
        self.rect.center = (
            HALF_WIDTH + math.sin(self.theta) * self.radius,
            HALF_HEIGHT + math.cos(self.theta) * self.radius
        )
        
        # gravity
        #self.gravity += 0.1
        
    def controls(self):
        keys = pg.key.get_pressed()
        
        #freezing the character so this code cant mess up something later
        #need to figure out how to display a game over screen cant get 'screen.blit to work or 'screen.fill' im probebly being stupid but
        #i cant figure it out
        if(self.speed_multiplier > 10):
            self.speed = 0 
            self.gravity = 0
            self.radius = 5
            
        # space bar controls
        if keys[pg.K_SPACE]:
            self.radius += 2
            self.gravity = 0
    
        # movement clockwise and anti-clockwise
        if keys[pg.K_LEFT]:
            self.theta += self.speed * self.speed_multiplier
            self.speed_multiplier += 0.2
        if keys[pg.K_RIGHT]:
            self.theta -= self.speed

        if(self.radius > 0 and not keys[pg.K_SPACE]):
            self.radius -= 2 * self.gravity

        