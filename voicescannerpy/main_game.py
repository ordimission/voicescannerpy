from core.command.ReadImageCommand import ReadImageCommand
from core.command.SayTextCommand import SayTextCommand
from core.command.SayTextPyttsxCommand import SayTextPyttsxCommand
from core.command.ScanImageCommand import ScanImageCommand
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640, 480))
goon = 1
paragraphs = ""
index = 0
image_path = "/tmp/image_test.jpg"
scanner = "brother"
engine = "picotts"

while goon:
    for event in pygame.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            print("Quit")
            goon = 0
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                SayTextCommand({"text": "Lecture en cours", "engine": engine}).execute()
                ScanImageCommand({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
                paragraphs = ReadImageCommand({"path": image_path, "lang": "fr_FR"}).execute()
                SayTextCommand({"text": str(len(paragraphs)) + " paragraphes", "engine": engine}).execute()
                print("Scan " + str(len(paragraphs))+ " paragraphes")
            if event.key == K_SPACE:
                SayTextCommand({"text": "position " + str(index+1) + " sur " + str(len(paragraphs)), "engine": engine}).execute()
                print("Space " + "position " + str(index+1) + " sur " + str(len(paragraphs)))
            if event.key == K_LEFT:
                if index > 0:
                    index = index - 1
                SayTextCommand(
                    {"text": paragraphs[index], "engine": engine}).execute()
                print("Left " + paragraphs[index])
            if event.key == K_RIGHT:
                if index < len(paragraphs) - 1:
                    index = index + 1
                SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
                print("Right " + paragraphs[index])
            if event.key == K_DOWN:
                SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
                print("Down " + paragraphs[index])
            if event.key == K_FIRST or event.key == K_PAGEUP:
                index = 0
                SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
                print("First " + paragraphs[index])
            if event.key == K_LAST or event.key == K_PAGEDOWN:
                index = len(paragraphs) - 1
                SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
                print("Last " + paragraphs[index])
