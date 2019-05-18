#!/usr/bin/env python
# coding=UTF-8

from core.ocr.ReadImageCommand import ReadImageCommand
from core.ocr.ScanImageCommand import ScanImageCommand
image_path = "/tmp/image_test.jpg"
text_path = r"/tmp/scan_output.txt"
scanner = "plustek"
voice_engine = "picotts"
read_image_engine = "google"

ScanImageCommand({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
text = ReadImageCommand({"path": image_path, "lang": "fr_FR", "engine": read_image_engine, "split": 1}).execute()
print (text)
f = open(text_path, "w")
for l in text:
    f.write(l.encode('utf8')+'\n')
f.close()
