#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import pyttsx3;


class VoiceOutputPyttsx(object):

    def __init__(self, args):
        self.lang = args.get('lang', 'fr-FR')
        self.path = args.get('path', '/tmp/output.wav')
        self.pitch = args.get('pitch', 50)
        self.amplitude = args.get('amplitude', 90)
        self.speed = args.get('speed', 100)
        self.espeak_path = args.get('espeak_path', '/usr/bin/espeak')

    def execute(self, text):
        engine = pyttsx3.init();
        engine.say(text);
        engine.runAndWait();


#main
#SayTextPyttsxCommand({"text": "Mon nom est Amélie Duermael."}).execute()