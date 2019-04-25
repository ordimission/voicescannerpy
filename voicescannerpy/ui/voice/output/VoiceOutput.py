#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import subprocess
import pyaudio
import wave
import StringIO
import sys
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

    def speak(self, text):
        if self.engine == 'espeak':
            espeak_command = [self.espeak_exec_path, '-v' + self.lang, '-s' + str(self.speed), '-a' + str(self.amplitude),
                             '-p' + str(self.pitch), '-w' + self.path, text]
            # generate the file with eSpeak
            subprocess.call(espeak_command, stderr=sys.stderr)
            f = wave.open(self.path, "rb")
        if self.engine == 'picotts':
            picotts = PicoTTS()
            picotts.voice = self.lang
            synth = picotts.synth_wav(text)
            w = StringIO.StringIO(synth)
            f = wave.open(w)

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



#main
#SayTextCommand({"text":"Mon nom est Amélie Duermael. Je suis votre assistante","engine":"espeak"}).execute()