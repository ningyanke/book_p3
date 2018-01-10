#!/usr/bin/evn python
# coding=utf-8
from __future__ import print_function
import os
import sys
from PIL import Image

"""
sys.argv[0] 是脚本的文件名称,
sys.argv[1:] 是要作用于的所有图片的名字
os.path.splitext  返回的是一个列表,前面是所有的内容,后面是扩展名

"""
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("不能转换格式")
    else:
        print("不需要转换格式")
