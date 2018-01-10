#!/usr/bin/env python
# coding=utf-8

"""
这是一个随机生成字母验证图片的小程序
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 生成随机字母,根据ASCII表中得到的数据为65-90为A-Z 的大写字母


def rndChar():
    return chr(random.randint(65, 90))

# 生成随机颜色1:


def rndColor():
    cor = (random.randint(64, 255), random.randint(
        64, 255), random.randint(64, 255))
    return cor

# 生成随机颜色2


def rndColor1():
    cor = (random.randint(64, 255), random.randint(
        64, 255), random.randint(64, 255))
    return cor


# 生成一个窗口
width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
# ubuntu的字体目录为/usr/share/fonts 随便从中取一款字体配对使用即可
font = ImageFont.truetype(
    font='/usr/share/fonts/opentype/stix/STIXGeneral-Bold.otf', size=36)
# 创建draw对象
draw = ImageDraw.Draw(img)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor1())


# 模糊
image = img.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
