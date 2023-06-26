"""
任务 3.3 判断相似矩阵的对角线元素是否均为 1（允许误差 10−6），如均
为 1 得 5 分，否则得 0 分。

"""
import  pandas as pd
import numpy as np
import  os

data = pd.read_excel("criteria3.xlsx")
t = data.columns.values
data_col = data.columns.values
def than(left,right):
    for i in range(left, right):
        flag =False
        name = "../dataA/A" + str(i) + "/task3.xlsx"
        s = 0
        data = pd.read_excel(name)
        l = []
        t = data.columns.values
        data_col = data.columns.values
        for k in range(data.shape[0]):
            l.append(data.loc[k][t[k + 1]])
        for o in l:
            if abs(float(float(o)-1)) >= 0.000001:
                flag=True
            else:
                flag = False
        if(flag):
            print(name + "分数：5")
        else:print(name+"分数：0")






"""
任务 3.4 判断相似矩阵的元素是否关于主对角线对称（允许误差 10
−6），
4
每出现一组不对称的元素，错误数 s 加 1。对错误数 s：s = 0 得 10 分，1 ≤ s ≤ 5
得 7 分，6 ≤ s ≤ 10 得 4 分，s ≥ 11 得 0 分。
"""

#遍历每个文件的task3.xlsx
for i in range(101,108):
    #判断task3.xlsx是否存在。
    s = 0
    if(os.path.exists("../dataA/A"+str(i)+"/task3.xlsx")):
        data_task = pd.read_excel("../dataA/A"+str(i)+"/task3.xlsx")
        #将列不规范的列删掉，留下有ID的列
        for z in data_task.columns.values:
            if "ID" not in z:
                #删除
                data_task.drop(z, axis=1, inplace=True)
        #转置矩阵
        data_task_T = data_task.T
        data_task_column = data_task.columns.values
        data_task_T_index = data_task_T.index.values
        # # print(data_task_column)
        for j in range(data_task.shape[0]):
            t1=str(data_task.loc[j][data_task_column[j]])
            t2 = str(data_task_T.loc[data_task_T_index[j]][j])
            if t1==t2:
                continue
            else:
                s+=1


"""
任务 3.5 以“criteria3.xlsx”为标准，统计相似矩阵上三角元素的错误数 s。
对每个匹配的元素计算绝对误差 e，0.005 ≤ e < 0.01，错误数 s 加 0.5；e ≥ 0.01，
错误数 s 加 1。对每个匹配不上的元素，错误数 s 加 1。对错误数 s：s = 0 得 15
分，1 ≤ s ≤ 5 得 10 分，6 ≤ s ≤ 10 得 5 分，s ≥ 11 得 0 分。

"""
#遍历每个文件的task3.xlsx
for i in range(101,108):
    #判断task3.xlsx是否存在。
    s = 0
    if(os.path.exists("../dataA/A"+str(i)+"/task3.xlsx")):
        data_task = pd.read_excel("../dataA/A"+str(i)+"/task3.xlsx")
        #将列不规范的列删掉，留下有ID的列
        for z in data_task.columns.values:
            if "ID" not in z:
                data_task.drop(z, axis=1, inplace=True)
        data_task_columnsss = data_task.columns.values
        for j in range(data_task.shape[0]-1):
            k = j+1
            #技术绝对误差
            while k<=data_task.shape[0]-1:
                t1=float(data.loc[j][data_col[k+1]])
                t=float(data_task.loc[j][data_task_columnsss[k]])
                sum_res =abs(t1-t)
                # print(sum_res)
                if sum_res>=0.005 and sum_res<0.01:
                    s+=0.5
                elif sum_res >=0.01:
                    s+=1
                else:sum_res+=1
                k+=1


if __name__ == '__main__':
    than(101,120)



