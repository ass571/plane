# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((480,700),0,32)
pygame.display.set_caption("hello, world!")
background = pygame.image.load('images/background.png').convert()
plane = pygame.image.load('images/life.png').convert_alpha()
class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
    def move(self):
        if self.y<0:
            mouseX,mouseY = pygame.mouse.get_pos()
            self.x=mouseX-self.image.get_width()/2
            self.y=mouseY-self.image.get_height()/2
        else:
            self.y -=20
bullet = Bullet()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    bullet.move()
    screen.blit(bullet.image,(bullet.x,bullet.y))
    x, y = pygame.mouse.get_pos()
    x-= plane.get_width()/2
    y-= plane.get_height()/2
    screen.blit(plane,(x,y))
    pygame.display.update()