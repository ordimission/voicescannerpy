
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640, 480))
goon = 1
while goon:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Quit")
            goon = 0
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                print("Scan")
            if event.key == K_LEFT:
                print("Left")
            if event.key == K_RIGHT:
                print("Right")
            if event.key == K_FIRST or event.key == K_PAGEUP:
                print("First")
            if event.key == K_LAST or event.key == K_PAGEDOWN:
                print("Last")
