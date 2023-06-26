"""
任务 2.1 通用名称评分
以“criteria2_1.xlsx”为标准，根据正式登记证号对每份作品中的“task2_1.xlsx”
进行匹配，按以下规则统计错误数：
(1) 对匹配的记录，判断“产品通用名称”是否一致，如不一致，错误数 s 加1。
"""
import  pandas as pd
import numpy as np
import os
data = pd.read_excel("criteria2_1.xlsx")
index = data.shape[0]
res = {}
def xunhuan(left,right):
    # 循环文件夹
    for i in range(left, right):
        s=0
        if os.path.exists("dataA/A" + str(i) + "/task2_1.xlsx"):
            data_task2_1 = pd.read_excel("dataA/A" + str(i) + "/task2_1.xlsx")
            name = "A" + str(i)
            #循环
            for j in range(index):
                s1 = str(data.iloc[j, 9]).replace("/t","").replace(" ","")
                for k in range(data_task2_1.shape[0]):
                    s2 = str(data_task2_1.iloc[k, 9]).replace("/t","").replace(" ","")
                    if s1 == s2:
                        s3 = str(data.iloc[j, 2]).replace("/t","").replace(" ","")
                        s4 = str(data_task2_1.iloc[k, 2]).replace("/t","").replace(" ","")
                        if s3 == s4:
                            break
                        else:
                            s += 1
            if s==0:
                res[name] = 15
            elif s>=1 and s<=10:
                res[name] = 10
            elif s>=11 and s<=20:
                res[name] = 5
            else:
                res[name] = 0
            print(str(name)+"--->"+str(res.get(name)))
            print()
res = xunhuan(101,120)




