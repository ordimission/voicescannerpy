#!/usr/bin/env python
# coding=UTF-8

from core.command.text.vision.ReadImageCommand import ReadImageCommand
from ui.output.SpeakerVoiceOutput import SpeakerVoiceOutput
from ui.input.KeyboardInput import *
from ui.input.ScannerInput import ScannerInput


goon = 1
paragraphs = ""
index = 0
image_path = "/tmp/image_test.jpg"
scanner = "plustek"
voice_engine = "picotts"
read_image_engine = "google"

voice_out = SpeakerVoiceOutput({"engine": voice_engine})
voice_out.speak("Mon nom est Amélie. Je suis votre assistante")
while goon:
    key = getch()
    if key == KEY_UP:
        print("Quit")
        goon = 0
    if key == KEY_ENTER:
        voice_out.speak("Lecture en cours")
        ScannerInput({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
        index = 0
        paragraphs = ReadImageCommand({"path": image_path, "lang": "fr_FR", "engine": read_image_engine}).execute()
        voice_out.speak(str(len(paragraphs)) + " paragraphes")
        print("Scan " + str(len(paragraphs))+ " paragraphes")
    if key == KEY_SPACE:
        voice_out.speak("position " + str(index + 1) + " sur " + str(len(paragraphs)))
        print("Space " + "position " + str(index+1) + " sur " + str(len(paragraphs)))
    if key == KEY_LEFT:
        if index > 0:
            index = index - 1
        voice_out.speak(paragraphs[index])
        print("Left " + paragraphs[index])
    if key == KEY_RIGHT:
        if index < len(paragraphs) - 1:
            index = index + 1
        voice_out.speak(paragraphs[index])
        print("Right " + paragraphs[index])
    if key == KEY_DOWN:
        voice_out.speak(paragraphs[index])
        print("Down " + paragraphs[index])
    if key == KEY_FIRST:
        index = 0
        voice_out.speak(paragraphs[index])
        print("First " + paragraphs[index])
    if key == KEY_LAST:
        index = len(paragraphs) - 1
        voice_out.speak(paragraphs[index])
        print("Last " + paragraphs[index])
