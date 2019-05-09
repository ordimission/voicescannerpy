#!/usr/bin/env python
from __future__ import print_function


class ReadImageCommand(object):

    def __init__(self, args):
        self.path = args.get('path', 'scanImage.jpg')
        self.lang = args.get('lang', 'fr_FR')
        self.engine = args.get('engine', 'tesseract')

    def execute(self):
        if self.engine == 'tesseract':
            from TesseractReadImageCommand import TesseractReadImageCommand
            return TesseractReadImageCommand({"path": self.path, "lang": self.lang}).execute()
        if self.engine == 'google':
            from GoogleReadImageCommand import GoogleReadImageCommand
            return GoogleReadImageCommand({"path": self.path, "lang": self.lang}).execute()


#main
#print(ReadImageCommand({"path": "/home/ordimission/Documents/test_cpdh.png", "lang": "fr_FR"}).execute())