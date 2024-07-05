import pygame as pg
from settings import *
import math


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.img = pg.image.load("assets/plane.png")
        self.rect = self.img.get_rect(center=HALF_RES)
        
        self.theta = 0
        self.radius = 10
    
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        self.movement()
        
    def movement(self):
        self.rect.x += math.sin(self.theta) * self.radius
        self.rect.y += math.cos(self.theta) * self.radius
        
        self.theta += 0.1
