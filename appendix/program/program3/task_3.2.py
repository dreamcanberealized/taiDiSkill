"""
任务 3.2 公司 ID 匹配
对相似矩阵进行匹配，按以下规则统计错误数：
(1) 对“criteria3.xlsx”中的每个公司 ID，查找“task3.xlsx”，如没有匹配的
公司 ID，错误数 s 加 1。
(2) 对“task3.xlsx”中的每个公司 ID，查找“criteria3.xlsx”，如没有匹配的
公司 ID，错误数 s 加 1。
对错误数 s：s = 0 得 15 分，1 ≤ s ≤ 2 得 10 分，3 ≤ s ≤ 5 得 5 分，s ≥ 6
得 0 分。
"""
#(1)
import  pandas as pd
import numpy as np
import  os
data = pd.read_excel("criteria3.xlsx")
s = 0
index = data.shape[0]
column=data.columns.values
#循环遍历
def id(left,right):
    for i in range(left, right):
        s = 0
        # 判断task3.xlsx是否存在。
        name = "../dataA/A" + str(i) + "/task3.xlsx"
        if (os.path.exists(name)):
            data_task = pd.read_excel(name)
            column_task3 = str(data_task.columns.values)
            # 遍历每个公司id 和这个task3.xlsx中id比较
            for j in column:
                if j in column_task3:
                    continue
                else:
                    s += 1
        else:
            continue
        sum = 0
        if s==0:
            sum = 15
        if s>=1 and s<=2:
            sum = 10
        if s>=3 and s<=5:
            sum = 5
        print(name+"分数："+str(sum))

"""
对“task3.xlsx”中的每个公司 ID，查找“criteria3.xlsx”，如没有匹配的
公司 ID，错误数 s 加 1。
"""
def idpi(left,right):
    for i in range(left, right):
        s=0
        # 判断task3.xlsx是否存在。
        name = "../dataA/A" + str(i) + "/task3.xlsx"
        if (os.path.exists("../dataA/A" + str(i) + "/task3.xlsx")):
            data_task = pd.read_excel("../dataA/A" + str(i) + "/task3.xlsx")
            column_task3 = data.columns.values
            # 遍历每个公司id 和这个task3.xlsx中id比较
            for j in column_task3:
                if "ID" in j:
                    if j in column:
                        continue
                    else:
                        s += 1
        else:
            continue
        sum = 0
        if s == 0:
            sum = 15
        if s >= 1 and s <= 2:
            sum = 10
        if s >= 3 and s <= 5:
            sum = 5
        print(name + "分数：" + str(sum))


if __name__ == '__main__':
    # id(101,419)
    idpi(101,419)




