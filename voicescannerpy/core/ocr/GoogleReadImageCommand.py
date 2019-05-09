#!/usr/bin/env python
from __future__ import print_function
from google.cloud import vision
import io


class GoogleReadImageCommand(object):

    def __init__(self, args):
        self.path = args.get('path', 'scanImage.jpg')
        self.lang = args.get('lang', 'fr_FR')

    def execute(self):
        """
           This function will handle the core OCR processing of images.
           """
        client = vision.ImageAnnotatorClient()

        with io.open(self.path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.document_text_detection(image=image)
        text = response.full_text_annotation.text
        return filter(lambda x: len(x) > 1, text.split('\n'))


#main
#print(GoogleReadImageCommand({"path": "/home/ordimission/Documents/test_cpdh.png", "lang": "fr_FR"}).execute())