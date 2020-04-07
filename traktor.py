import pygame
from pygame.math import Vector2

class Traktor(object):
    
    def __init__(self, game):
        #przekazywanie okiektu gra obiektowi traktor
        self.game = game

        self.pozycja = Vector2(0,0)
        

    def tick(self):
        #kliknięcia
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.pozycja.y -= 5
        if pressed[pygame.K_DOWN]:
            self.pozycja.y += 5
        if pressed[pygame.K_RIGHT]:
            self.pozycja.x += 5
        if pressed[pygame.K_LEFT]:
            self.pozycja.x -= 5
        

        
    def rysowanie(self):
        rect = pygame.Rect(self.pozycja.x, self.pozycja.y ,50,50)
        pygame.draw.rect(self.game.pole, (0,150,255), rect)