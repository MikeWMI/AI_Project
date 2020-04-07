import pygame, sys
from traktor import Traktor

class Game(object):
    
    def __init__(self):
    
        #inicjalizacja
        pygame.init()
        self.pole = pygame.display.set_mode((1000,720))

        self.player = Traktor(self)

        while True:
            #obsługa zdarzń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.tick()
            #rysowanie
            self.pole.fill((0,0,0))
            self.rysowanie()
            pygame.display.flip()


    def tick(self):
        #sprawdzanie klikniecia
        
        self.player.tick()

        
    def rysowanie(self):
        #rysowanie
        self.player.rysowanie()
        

if __name__=="__main__":
    Game()




    


    