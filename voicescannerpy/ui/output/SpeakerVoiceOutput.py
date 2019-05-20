#!/usr/bin/env python
# coding=UTF-8
import os
from voicescannerpy.ui.output.SpeakerOutput import SpeakerOutput
from voicescannerpy.core.command.sound.speech.TextToSpeechCommand import TextToSpeechCommand


class SpeakerVoiceOutput(TextToSpeechCommand):

    def __init__(self, args):
        TextToSpeechCommand.__init__(self, args)

    # generates a wave
    def speak(self, text):
        if os.name == 'nt':
            self.execute(text)
        else:
            f = self.execute(text)
            SpeakerOutput().play(f)


