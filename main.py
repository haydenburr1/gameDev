import pygame as pg 
import sys

FPS = 60

class App:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((800, 400))
        self.clock = pg.time.Clock()
    
    def game_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def draw(self):
        pass
    
    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        
    def run(self):
        while True:
            self.game_loop()
            self.draw()
            self.update()
            
if __name__ == "__main__":
    app = App()
    app.run()
    