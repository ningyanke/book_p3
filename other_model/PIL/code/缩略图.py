#!/usr/bin/env python
# coding=utf-8

"""
glob 是python的标准模块
是一种智能化的文件名匹配基数,在图像处理中经常会用到
"""

from PIL import Image
import glob
import os

size = (128, 128)
for infile in glob.glob('test1.jpg'):
    f, ext = os.path.split(infile)
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(f + 'suoluotu' + '.png')
