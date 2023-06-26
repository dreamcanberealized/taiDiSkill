"""
(2) 对“criteria2_2.xlsx”中的每条记录，查找“task2_2.xlsx”，如没有匹配
的记录，错误数 s 加 1。
"""
import  pandas as pd
import numpy as np
import  os
data = pd.read_excel("criteria2_2.xlsx")
index = data.shape[0]
s = 0
res = {}

res = {}
def criteria2_2(left,right):
    # 循环文件夹
    for i in range(left, right):
        s=0
        if os.path.exists("dataA/A" + str(i) + "/task2_2.xlsx"):
            data_task2_1 = pd.read_excel("dataA/A" + str(i) + "/task2_2.xlsx")
            name = "A" + str(i)
            for j in range(index):
                flag = False
                s1 = str(data.iloc[j, 9]).replace("/t","").replace(" ","")
                for k in range(data_task2_1.shape[0]):
                    s2 = str(data_task2_1.iloc[k, 9]).replace("/t","").replace(" ","")
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
        res = criteria2_2(200,215)