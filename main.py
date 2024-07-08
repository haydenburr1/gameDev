import pygame as pg 
from settings import *
import sys
from sprites import Player, Enemy


class App:
    def __init__(self):
        pg.init() 
        
        # variables for screen creation
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
    
        # variables for blitting
        self.player = Player()
        self.enemy_list = [Enemy() for _ in range(NO_OF_ENEMIES)]
        
        # planet vars
        self.planet_surf = pg.image.load("assets/planet2.png").convert_alpha()
        self.planet_rect = self.planet_surf.get_rect(center=HALF_RES)

    @staticmethod
    def game_loop():
        # basic game loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def draw(self):
        # blitting to the screen. avoid anything else in this method 
        self.screen.fill("black")
        self.screen.blit(self.planet_surf, self.planet_rect)
        self.player.draw(self.screen)

        for enemy in self.enemy_list:
            enemy.draw(self.screen)

    def collisions(self):
        if self.planet_rect.colliderect(self.player.rect):
            self.player.gravity = 0
        
        #pg.sprite.spritecollide(self.player, self.enemy_list, True)

    def update(self):
        # for updating rects and other variables, do it here 
        pg.display.update()
        self.clock.tick(FPS)
        pg.display.set_caption(f"fps: {self.clock.get_fps():.2f}")
        
    def run(self):
        while True:
            # add functions as per...
            self.game_loop()
            self.collisions()
            self.draw()
            self.update()


if __name__ == "__main__":
    app = App()
    app.run()
