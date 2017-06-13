#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/12 14:56
# @Author  : Liang
# @Site    : matrixbingo@gmail.com
# @File    : asas.py
# @Software: PyCharm

from PIL import Image
im = Image.open('D:/ppd.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))
im.save('D:/thumb.jpg', 'JPEG')