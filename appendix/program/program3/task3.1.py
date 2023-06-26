"""
任务 3 相似矩阵评分
以“criteria3.xlsx”为标准，对每份作品“task3.xlsx”中的相似矩阵（以下简
称相似矩阵）按以下规则进行评分。
任务 3.1 判断相似矩阵的维数与“criteria3.xlsx”中的是否一致，如一致得
5 分，否则得 0 分。
"""

#一致
import  pandas as pd
import numpy as np
import os
data = pd.read_excel("criteria3.xlsx")
shape = str(data.shape)
ndim = str(data.ndim)

def juzhen(left,right):
    for i in range(left, right):
        name = "../dataA/A" + str(i) + "/task3.xlsx"
        s = 0
        if os.path.exists(name):
            data_task2_1 = pd.read_excel("../dataA/A" + str(i) + "/task3.xlsx")
            shape_2 = str(data_task2_1.shape)
            ndim_2 = str(data_task2_1.ndim)
            if shape == shape_2 and ndim == ndim_2:
                print(name+str("分数5"))
            else:print(name+str("分数0"))
if __name__ == '__main__':
    juzhen(101,120)
