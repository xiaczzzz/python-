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
import numpy as np
import matplotlib.pyplot as plt
import math
code_num = 20
Rs = 1000
Rc = 2* Rs
sampling = 0.01
t = np.arange(0,code_num/Rs,sampling/Rs)
Data_length = len(t)
code = np.random.randint(0,2,code_num)
Ask_base = np.zeros(Data_length)
for i in range(Data_length):
    Ask_base [i]= code[math.floor(t[i]* Rs)]
carrier = np.cos(2* math.pi* Rc* t)
Ask_m = np.multiply(carrier,Ask_base)
fig = plt.figure(figsize = (8,6))
ASK_3 = fig.add_subplot()
plt.plot(t,Ask_m,'b')
plt.show()