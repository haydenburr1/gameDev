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
        
        self.test_surf = pg.image.load("assets/plane.png")
        self.test_rect = self.test_surf.get_rect(center=HALF_RES)
        
    def game_loop(self):
        # basic game loop
        # TODO: controls for when neded 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def draw(self):
        # blitting to the screen. avoid anything else in this method 
        self.screen.fill("white")
        #self.screen.blit(self.font_surf, self.font_rect)
        self.player.draw(self.screen)
        
    def update(self):
        # for updating rects and other variables, do it here 
        pg.display.update()
        self.clock.tick(FPS)
        
    def run(self):
        while True:
            # add functions as per...
            self.game_loop()
            self.draw()
            self.update()

# needed to run
if __name__ == "__main__":
    app = App()
    app.run()
