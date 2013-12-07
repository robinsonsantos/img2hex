#! /usr/bin/env python
# *-* coding: utf-8 *-*


#TODO remove old code
#TODO use command line parameter
#TODO use graphic interface option
#TODO use not only bmp files
#TODO choose size output
#TODO use OOP

import Image
import ImageColor

bmp_img  = 'tux04.bmp'
vetor_c =  'tux05.c'

f = open(vetor_c,'w')
i = Image.open(bmp_img)

x = 0
y = 0
z = 0
octet = 0

f.write('const unsigned char ')
f.write('tux04')
#f.write('[ ')
#f.write(str(x+y))
#f.write(' ] = {\n\t')

f.write('[] = {\n\t')


while y < 128:
    x = 0
    while x < 240:
        for j in range(8):
            z = i.getpixel((x,y))

            if (j == 0):
                octet = (z & 1)
            else:
                octet = octet << 1
                octet = octet | (z & 1)

            x = x + 1

        octet = hex(octet)   
        f.write(str(octet))
        f.write(', ')

    y = y + 1
    f.write('\n\t')

f.write('};')
f.write('\n')
f.close()
