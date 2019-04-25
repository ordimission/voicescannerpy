#!/usr/bin/env python
""" generated source for module ScanImageCommand """
from __future__ import print_function
from pyScanLib import pyScanLib


class ScanImageCommand(object):

    def __init__(self, args):
        self.path = args.get('path', 'scanImage.jpg')
        self.resolution = args.get('dpi', 150)
        self.mode = args.get('mode', 'gray')
        self.scanner = args.get('scanner', None)

    def execute(self):
        scanLib = pyScanLib()

        try:
            scanLib.setScanner(self.scanner)
        except:
            scanners = scanLib.getScanners()
            found = False
            print('Available scanners:', scanners)
            for scanner in scanners:
                print(scanner)
                if isinstance(scanner, tuple):
                    # sane
                    scanner_name = scanner[0]
                else:
                    # twain
                    scanner_name = scanner
                if scanner_name.startswith(self.scanner):
                    scanLib.setScanner(scanner_name)
                    found = True
            if not found and scanners:
                if isinstance(scanners[0], tuple):
                    # sane
                    scanLib.setScanner(scanners[0][0])
                else:
                    # twain
                    scanLib.setScanner(scanners[0])


        scanLib.setDPI(self.resolution)

        scanLib.setScanArea(left=0, top=0, width=8.267, height=11.693) #(left,top,width,height)
        # scanLib.setPixelType(self.mode)  # bw/gray/color
        #
        pil = scanLib.scan()
        pil.save(self.path)
        scanLib.closeScanner()  # unselect selected scanner input setScanners()
        scanLib.close()  # Destory whole class


#main
#ScanImageCommand({"path": "/tmp/image_test.jpg", "scanner": "plustek", "mode": "color"}).execute()
