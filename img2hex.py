#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TODO use command line parameter
#TODO verify dependencies, otherwise suggest install
#TODO use not only bmp files
#TODO use output file define by user
#TODO convert image to grayscale
#TODO resize image

import sys
import re
import Image

FILE_NAME  = 1
MAX_ROW    = 128
MAX_COLUMN = 240

class Img2hex(object):
    ''' None '''
    def __init__(self):
        self.__img_file = None
        self.__hex_file = None

    def open_img(self, img_file):
        try:
            self.__img_file = Image.open(img_file)
            print 'Image file opened sucessfully'
        except:
            print 'Could not open the image file'
            sys.exit()
 
    def open_hex(self, hex_file):
        try:
            self.__hex_file = open(hex_file, 'w')
            print 'Hex file opened sucessfully'
        except:
            print 'Could not open the hex file'
            sys.exit()

    def convert_to_grayscale(self):
        pass
          
    def generate(self):
        column = 0
        row = 0
        rgb_value = 0
        octet = 0
        self.__hex_file.write('const unsigned char ')
        self.__hex_file.write('tux04')
        self.__hex_file.write('[] = {\n\t')

        while row < MAX_ROW:
            column = 0
            while column < MAX_COLUMN:
                rgb_value = self.__img_file.getpixel((column, row))
                for i in xrange(8):
                    if (i == 0):
                        octet = (rgb_value & 1)
                    else:
                        octet = octet << 1
                        octet = octet | (rgb_value & 1)
                    column = column + 1
                octet = hex(octet)
                self.__hex_file.write(str(octet))
                self.__hex_file.write(', ')
            row = row + 1
            self.__hex_file.write('\n\t')
        self.__hex_file.write('};')
        self.__hex_file.write('\n')
        self.__hex_file.close()

def main():
    if len(sys.argv) == 2:
        print 'Begin'
        img2hex = Img2hex()
        img2hex.open_img(sys.argv[FILE_NAME])
        img2hex.open_hex('teste2.c')
        img2hex.generate()
        print 'End'

if __name__ == "__main__":
    main()
