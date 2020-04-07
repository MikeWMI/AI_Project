import math
import pygame
import tkinter
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass


class snake(object):
    turns = {}
    def __init__(self, color, position):
        self.color = color
        self.head = cube(position)

        #kierunek ruchu węża
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        pass
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    #aktualan pozycja głowy- traktora
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    #aktualan pozycja głowy- traktora
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    #aktualan pozycja głowy- traktora
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    #aktualan pozycja głowy- traktora
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
        """
       


    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w  // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        # (x,0), (0,y) - początkowe pozycje 
        # (x,w), (x,y) - końcowe pozycje
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (x,y))

def message_box(subject, contetnt):
    pass

def redrawWindow(surface):
    surface.fill((0,0,0))  # Fills the screen with black
    drawGrid(surface)  # Will draw our grid lines
    pygame.display.update()  # Updates the screen

def main():
    global rows, width, s
    width = 500
    height = 500
    rows = 10
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (1,1))
    #clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(50)
        #clock.tick(10)
        redrawWindow(win)
    pass

main()
