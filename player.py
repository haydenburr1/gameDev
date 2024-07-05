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
        self.radius = 200
        self.speed = 0.1
        
        # Load the image and set the rect
        self.img = pg.image.load("assets/plane.png").convert_alpha()
        self.rect = self.img.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
    
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        self.movement()
    
    def movement(self):
        # Update the position based on theta and radius
        self.rect.center = (
            HALF_WIDTH + math.sin(self.theta) * self.radius,
            HALF_HEIGHT + math.cos(self.theta) * self.radius
        )
        
        # Increment theta to move
        self.theta += self.speed
