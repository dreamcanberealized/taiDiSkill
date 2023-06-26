"""
(3) 对“task2_2.xlsx”中的每条记录，查找“criteria2_2.xlsx”，如没有匹配
的记录，错误数 s 加 1。
"""
import  pandas as pd
import numpy as np
data = pd.read_excel("criteria2_2.xlsx")
import os
index = data.shape[0]
s = 0
res = {}
def task2_2(left,right):
    # 循环文件夹
    for i in range(left, right):
        s=0
        if os.path.exists("dataA/A" + str(i) + "/task2_2.xlsx"):
            data_task2_2 = pd.read_excel("dataA/A" + str(i) + "/task2_2.xlsx")
            name = "A" + str(i)
            #遍历task2_2.xlsx
            for j in range(data_task2_2.shape[0]):
                s2 = str(data_task2_2.iloc[j, 9]).replace("/t", "").replace(" ", "")
                flag = False
                # 遍历“criteria2_1.xlsx
                for k in range(index):
                    s1 = str(data.iloc[k, 9]).replace("/t", "").replace(" ", "")
                    if s1 == s2:
                        flag=True
                        break
                if flag==False:
                    s+=1
            if s==0:
                res[name] = 15
            elif s>=1 and s<=10:
                res[name] = 10
            elif s>=11 and s<=20:
                res[name] = 5
            else:
                res[name] = 0
        print(str(name) + "--->" + str(res.get(name)))

if __name__ == '__main__':
        res = task2_2(360,419)