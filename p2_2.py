# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:56:46 2021

@author: Mahsa
"""

from PIL import Image

img = Image.open('path/car_new.jpg')

img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("path/car_new_transparent.png", "PNG")