"""
任务 2.2 分组标签评分
以“criteria2_2.xlsx”为标准，根据正式登记证号对每份作品中的“task2_2.xlsx”
进行匹配，按以下规则统计错误数：
(1) 对匹配的记录，判断“分组标签”中的数值和顺序是否一致，如不一致，
错误数 s 加 1。
"""
import  pandas as pd
import numpy as np
import os
data = pd.read_excel("criteria2_2.xlsx")
index = data.shape[0]
res = {}

def fenzu(left,right):
    for i in range(left,right):
        if os.path.exists("dataA/A" + str(i) + "/task2_2.xlsx"):
            data_task2_2 = pd.read_excel("dataA/A"+str(i)+"/task2_2.xlsx")
            s = 0
            name = "A" + str(i)
            flag = False
            for j in range(index):
                s1 = str(data.iloc[j, 9])
                for k in range(data_task2_2.shape[0]):
                    s2 = str(data_task2_2.iloc[k, 9])
                    #判断
                    if s1 == s2:
                        s3 = "("+str(data.iloc[j, 15])+","+str(data.iloc[j, 16])
                        s4 = str(data_task2_2.iloc[k,15])
                        if s3 == s4:
                            flag=True
                            break
                if flag==False:
                    s+=1
            #计算分数
            if s == 0:
                res[name] = 15
            elif s >= 1 and s <= 10:
                res[name] = 10
            elif s >= 11 and s <= 20:
                res[name] = 5
            else:
                res[name] = 0
            print(str(name) + "--->" + str(res.get(name)))
if __name__ == '__main__':
        fenzu(120,140)
