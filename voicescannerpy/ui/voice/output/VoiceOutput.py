#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import sys
import os
if os.name == 'nt':
    import pyttsx3
else:
    import wave
    import subprocess
    import StringIO
    from picotts import PicoTTS


class VoiceOutput(object):

    def __init__(self, args):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.lang = args.get('lang', 'fr-FR')
        self.path = args.get('path', r"/tmp/output.wav")
        self.pitch = args.get('pitch', 50)
        self.amplitude = args.get('amplitude', 90)
        self.speed = args.get('speed', 100)
        self.espeak_exec_path = args.get('espeak_exec_path', r"/usr/bin/espeak")
        self.engine = args.get('engine', 'espeak')

        if os.name == 'nt':
            self.voice_output_engine = pyttsx3.init()
            if self.lang == 'fr-FR' or self.lang == 'fr_FR':
                voice = self.voice_output_engine.getProperty('voices')[0]  # the french voice
                self.voice_output_engine.setProperty('voice', voice.id)
        else:
            if self.engine == 'picotts':
                self.voice_output_engine = PicoTTS()
                self.voice_output_engine.voice = self.lang

    def speak(self, text):
        if os.name == 'nt':
            self.voice_output_engine.say(text)
            self.voice_output_engine.runAndWait()
        else:
            if self.engine == 'espeak':
                espeak_command = [self.espeak_exec_path, '-v' + self.lang, '-s' + str(self.speed), '-a' + str(self.amplitude),
                                 '-p' + str(self.pitch), '-w' + self.path, text]
                # generate the file with eSpeak
                subprocess.call(espeak_command, stderr=sys.stderr)
                f = wave.open(self.path, "rb")
            if self.engine == 'picotts':
                self.voice_output_engine = PicoTTS()
                self.voice_output_engine.voice = self.lang
                synth = self.voice_output_engine.synth_wav(text)
                w = StringIO.StringIO(synth)
                f = wave.open(w)
            self.play(f)

    def play(self, f):
        import pyaudio
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)

        # define stream chunk
        chunk = 1024
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

