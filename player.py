import pygame as pg
from settings import *
import math

import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        # Initialize parameters
        self.theta = 0
        self.radius = 200 # pixels
        self.speed = 0.05

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
        self.gravity += 0.1
        
    def controls(self):
        keys = pg.key.get_pressed()
        # space bar controls
        if keys[pg.K_SPACE]:
            self.radius += 2
            self.gravity = 0
    
        # movement clockwise and anti-clockwise
        if keys[pg.K_LEFT]:
            self.theta += self.speed
        if keys[pg.K_RIGHT]:
            self.theta -= self.speed

        if(self.radius > 0 and not keys[pg.K_SPACE]):
            self.radius -= 2 * self.gravity

        
    
