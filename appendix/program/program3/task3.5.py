"""
任务 3.5 以“criteria3.xlsx”为标准，统计相似矩阵上三角元素的错误数 s。
对每个匹配的元素计算绝对误差 e，0.005 ≤ e < 0.01，错误数 s 加 0.5；e ≥ 0.01，
错误数 s 加 1。对每个匹配不上的元素，错误数 s 加 1。对错误数 s：s = 0 得 15
分，1 ≤ s ≤ 5 得 10 分，6 ≤ s ≤ 10 得 5 分，s ≥ 11 得 0 分。

"""
import  pandas as pd
import numpy as np
import  os

data = pd.read_excel("criteria3.xlsx")
t = data.columns.values
data_col = data.columns.values
#遍历每个文件的task3.xlsx
def t(left,right):
    for i in range(left, right):
        # 判断task3.xlsx是否存在。
        s = 0
        if (os.path.exists("../dataA/A" + str(i) + "/task3.xlsx")):
            data_task = pd.read_excel("../dataA/A" + str(i) + "/task3.xlsx")
            # 将列不规范的列删掉，留下有ID的列
            for z in data_task.columns.values:
                if "ID" not in z:
                    data_task.drop(z, axis=1, inplace=True)
            data_task_columnsss = data_task.columns.values
            for j in range(data_task.shape[0] - 1):
                k = j + 1
                # 技术绝对误差
                while k <= data_task.shape[0] - 1:
                    t1 = float(data.loc[j][data_col[k + 1]])
                    t = float(data_task.loc[j][data_task_columnsss[k]])
                    sum_res = abs(t1 - t)
                    # print(sum_res)
                    if sum_res >= 0.005 and sum_res < 0.01:
                        s += 0.5
                    elif sum_res >= 0.01:
                        s += 1
                    else:
                        sum_res += 1
                    k += 1
                    print(s)
t(109,401)