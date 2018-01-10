#!/usr/bin/env python
# coding=utf-8

from PIL import Image
from PIL import ImageFilter
img = Image.open("2.png")
test1 = img.filter(ImageFilter.EMBOSS)
test1.show()
