#!/usr/bin/env python
from __future__ import print_function
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class ReadImageCommand(object):

    def __init__(self, args):
        self.path = args.get('path', 'scanImage.jpg')
        self.lang = args.get('lang', 'fr_FR')

    def execute(self):
        l = None
        if self.lang== 'fr' or self.lang.startswith('fr_'):
            l = 'fra'
        if self.lang == 'en' or self.lang.startswith('en_'):
            l = 'eng'
        if l is None:
            text = pytesseract.image_to_string(Image.open(self.path))
        else:
            text = pytesseract.image_to_string(Image.open(self.path), lang=l)
        # We'll use Pillow's Image class to open the image and pytesseract to detect the string input the image
        return filter(lambda x: len(x) > 1, text.split('\n\n'))


#main
#print(ReadImageCommand({"path": "/home/ordimission/Documents/test_cpdh.png", "lang": "fr_FR"}).execute())