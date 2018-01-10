#!/usr/bin/env python
# coding=utf-8

from PIL import Image


im = Image.open('test1.jpg')
"""
矩形选区有一个4元元组,分别表示,左上,右下,(from_x, from_y, to_x, to_y)左上角为原点,单位是px
"""

# 复制一个200*200的矩形区域

box = (100, 100, 300, 300)

region = im.crop(box)
region.show()
