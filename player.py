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
        self.controls()
        
    def movement(self):
        player_pos = pg.Vector2(WIDTH +math.sin(self.theta) * self.radius,  HEIGHT + math.cos(self.theta) * self.radius)
        self.rect.x += player_pos.x
        self.rect.y += player_pos.y
        
    def controls(self):
        # TODO
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.radius += 1
        
        
