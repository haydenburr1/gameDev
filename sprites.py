import pygame as pg
from settings import *
import math
from random import randint, choice


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        # Initialize parameters
        self.theta = 0
        self.radius = 200  # pixels
        self.speed = 0.05
        self.speed_multiplier = 0

        self.gravity = 0

        # Load the image and set the rect
        self.img = pg.image.load("assets/plane.png").convert_alpha()
        self.rect = self.img.get_rect(center=HALF_RES)

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

        # self.gravity += 0.1

    def controls(self):
        keys = pg.key.get_pressed()

        if self.radius > 0 and not keys[pg.K_SPACE]:
            self.radius -= self.gravity

        if self.speed_multiplier > MAX_SPEED:
            self.speed_multiplier = MAX_SPEED

        # space bar controls
        if keys[pg.K_SPACE]:
            self.radius += RADIUS_INCREMENT
            self.gravity = 0

        # movement clockwise and anti-clockwise
        if keys[pg.K_LEFT]:
            self.theta += self.speed * self.speed_multiplier
            self.speed_multiplier += SPEED_MULTIPLIER_INCREMENT

        if keys[pg.K_RIGHT]:
            self.theta -= self.speed * self.speed_multiplier
            self.speed_multiplier += SPEED_MULTIPLIER_INCREMENT

        if not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
            self.speed_multiplier = 0

        # this can be used for debugging

        if keys[pg.K_DOWN]:
            self.radius -= 2
        if keys[pg.K_UP]:
            self.radius += 2


class Enemy(pg.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()

        img_list = [
            r"assets/pixel_ship_blue_small.png",
            r"assets/pixel_ship_green_small.png",
            r"assets/pixel_ship_red_small.png"
        ]

        self.radius = 300  # pixels
        self.speed = randint(1, 3) / 10

        self.theta = randint(0, 360)

        self.image = pg.image.load(choice(img_list))
        self.rect = self.image.get_rect(center=HALF_RES)

    def draw(self, screen):
        self.rect.center = (
            HALF_WIDTH + math.sin(self.theta) * self.radius,
            HALF_HEIGHT + math.cos(self.theta) * self.radius
        )

        screen.blit(pg.transform.rotate(self.image, math.degrees(self.theta)), self.rect)

        self.radius -= self.speed
