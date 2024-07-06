import pygame as pg 
from settings import *
import sys
from player import Player

class App:
    def __init__(self):
        pg.init() 
        
        # variables for screen creation
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
    
        # variables for blitting
        self.player = Player()
        #planet vars
        self.planet_surf = pg.image.load("assets/planet2.png").convert_alpha()
        self.planet_rect = self.planet_surf.get_rect(center=HALF_RES)
        
    def game_loop(self):
        # basic game loop
        # TODO: controls for when neded 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def draw(self):
        # blitting to the screen. avoid anything else in this method 
        self.screen.fill("black")
        self.screen.blit(self.planet_surf,self.planet_rect)        
        self.player.draw(self.screen)
        
        if self.planet_rect.colliderect(self.player.rect):
            print("game over")
    
    
    def update(self):
        # for updating rects and other variables, do it here 
           pg.display.update()
           self.clock.tick(FPS)
           pg.display.set_caption(f"fps: {self.clock.get_fps():.2f}")
        
    def run(self):
        while True:
           # add functions as per...
            self.game_loop()
            self.draw()
            self.update()

if __name__ == "__main__":
    app = App()
    app.run()
