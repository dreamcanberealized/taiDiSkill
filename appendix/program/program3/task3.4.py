"""
任务 3.4 判断相似矩阵的元素是否关于主对角线对称（允许误差 10
−6），
4
每出现一组不对称的元素，错误数 s 加 1。对错误数 s：s = 0 得 10 分，1 ≤ s ≤ 5
得 7 分，6 ≤ s ≤ 10 得 4 分，s ≥ 11 得 0 分。
"""
import  pandas as pd
import numpy as np
import  os

data = pd.read_excel("criteria3.xlsx")
t = data.columns.values
data_col = data.columns.values
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
