from core.ocr.ReadImageCommand import ReadImageCommand
from voicescannerpy.ui.voice.output.VoiceOutput import VoiceOutput
from core.ocr.ScanImageCommand import ScanImageCommand
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640, 480))
goon = 1
paragraphs = ""
index = 0
image_path = "image_test.jpg"
scanner = "Samsung"
engine = "picotts"

voice_out = VoiceOutput({"engine": engine})

while goon:
    for event in pygame.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            print("Quit")
            goon = 0
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                voice_out.speak("Lecture en cours")
                ScanImageCommand({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
                paragraphs = ReadImageCommand({"path": image_path, "lang": "fr_FR"}).execute()
                voice_out.speak(str(len(paragraphs)) + " paragraphes")
                print("Scan " + str(len(paragraphs)) + " paragraphes")
            if event.key == K_SPACE:
                voice_out.speak("position " + str(index + 1) + " sur " + str(len(paragraphs)))
                print("Space " + "position " + str(index+1) + " sur " + str(len(paragraphs)))
            if event.key == K_LEFT:
                if index > 0:
                    index = index - 1
                voice_out.speak(paragraphs[index])
                print("Left " + paragraphs[index])
            if event.key == K_RIGHT:
                if index < len(paragraphs) - 1:
                    index = index + 1
                voice_out.speak(paragraphs[index])
                print("Right " + paragraphs[index])
            if event.key == K_DOWN:
                voice_out.speak(paragraphs[index])
                print("Down " + paragraphs[index])
            if event.key == K_FIRST or event.key == K_PAGEUP:
                index = 0
                voice_out.speak(paragraphs[index])
                print("First " + paragraphs[index])
            if event.key == K_LAST or event.key == K_PAGEDOWN:
                index = len(paragraphs) - 1
                voice_out.speak(paragraphs[index])
                print("Last " + paragraphs[index])
