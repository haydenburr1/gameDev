import pygame as pg
from settings import *
import math


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.theta = 0
        self.radius = 10
        
        self.img = pg.image.load("assets/plane.png")
        self.rect = self.img.get_rect(center=(HALF_WIDTH - (math.sin(self.theta) * 100), HALF_HEIGHT - (math.cos(self.theta) * 100)))

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
        
        self.movement()
        
    def movement(self):
        # player_pos = pg.Vector2(HALF_WIDTH + math.sin(self.theta) * self.radius,  HALF_HEIGHT + math.cos(self.theta) * self.radius)
        self.rect.x += math.cos(self.theta) * self.radius
        self.rect.y += math.sin(self.theta) * self.radius
        
        
        self.theta += 0.1
