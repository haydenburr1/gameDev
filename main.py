import pygame as pg 
from settings import *
import sys

class App:
    def __init__(self):
        pg.init() 
        
        # variables for screen creation
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 50)
        
        # variables for blitting
        self.font_surf = self.font.render("hello world", False, (255, 255, 255))
        self.font_rect = self.font_surf.get_rect(center=(HALF_RES))
       
    def game_loop(self):
        # basic game loop
        # TODO: controls for when neded 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def draw(self):
        # blitting to the screen. avoid anything else in this method 
        self.screen.blit(self.font_surf, self.font_rect)
    
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
