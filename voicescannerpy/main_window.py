#!/usr/bin/env python
# coding=UTF-8

from core.ocr.ReadImageCommand import ReadImageCommand
from ui.voice.output.VoiceOutput import VoiceOutput
from core.ocr.ScanImageCommand import ScanImageCommand
import pygame
from pygame.locals import *


def display_text(str):
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render(str, True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text,
                (X // 2 - text.get_width() // 2, Y // 2 - text.get_height() // 2))
    pygame.display.flip()


pygame.init()
X = 640
Y = 480
screen = pygame.display.set_mode((X, Y))
# set the pygame window name
pygame.display.set_caption('Voice scanner')


goon = 1
paragraphs = ""
index = 0
image_path = "image_test.jpg"
scanner = "Samsung"
voice_engine = "picotts"
read_image_engine = "tesseract"

voice_out = VoiceOutput({"engine": voice_engine})
voice_out.speak("Mon nom est Amélie. Je suis votre assistante")
while goon:
    for event in pygame.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            print("Quit")
            goon = 0
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                voice_out.speak("Lecture en cours")
                display_text("Lecture en cours")
                ScanImageCommand({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
                paragraphs = ReadImageCommand({"path": image_path, "lang": "fr_FR", "engine": read_image_engine}).execute()
                voice_out.speak(str(len(paragraphs)) + " paragraphes")
                display_text("Scan " + str(len(paragraphs)) + " paragraphes")
            if event.key == K_SPACE:
                voice_out.speak("position " + str(index + 1) + " sur " + str(len(paragraphs)))
                display_text("position " + str(index+1) + " sur " + str(len(paragraphs)))
            if event.key == K_LEFT:
                if index > 0:
                    index = index - 1
                voice_out.speak(paragraphs[index])
                display_text(paragraphs[index])
            if event.key == K_RIGHT:
                if index < len(paragraphs) - 1:
                    index = index + 1
                voice_out.speak(paragraphs[index])
                display_text(paragraphs[index])
            if event.key == K_DOWN:
                voice_out.speak(paragraphs[index])
                display_text(paragraphs[index])
            if event.key == K_FIRST or event.key == K_PAGEUP:
                index = 0
                voice_out.speak(paragraphs[index])
                display_text(paragraphs[index])
            if event.key == K_LAST or event.key == K_PAGEDOWN:
                index = len(paragraphs) - 1
                voice_out.speak(paragraphs[index])
                display_text(paragraphs[index])


