# coding:utf-8
'''
Python 3.7
作者：夏成卓
日期：2022年06月05日
学校：BUPT
学院：电子工程学院
班级：2019211206
学号：2019210916
'''
import imageio
import numpy as np
import os
os.chdir('D:/Code/Python/python论文实例/data')  # 设置文件读取和保存位置

images = []
for i in range(64):
    image = str(i)+'.jpg'
    im = imageio.imread(image)
    images.append(im)
imageio.mimsave("a.gif", images, 'GIF', duration=0.1)  # durantion是延迟时间