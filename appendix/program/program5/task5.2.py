#导入模块
import os
import pandas as pd
#待搜索的名称
filename1 = "task2_1.xlsx"
filename2 = "task2_2.xlsx"
filename3 = "task2_3.pdf"
filename4 = "task3.xlsx"

result = []

def findfiles(path):
    print(os.listdir(path))
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for file in file_list:
    	# 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            findfiles(cur_path)
        else:
        	# 判断是否是特定文件名称
            if filename1 in file:
                result.append(file)
            elif filename2 in file:
                result.append(file)
            elif filename3 in file:
                result.append(file)
            elif filename4 in file:
                result.append(file)


bigArr = []

if __name__ == '__main__':
    path = 'D:\\桌面\\泰迪杯数据分析A题\\unDataB'
    file_list = os.listdir(path)
    print(file_list)
    # 遍历文件夹文件并寻找对应文件
    for file in file_list:
        result = []
        print(file)
        findfiles(path + '\\' + file)
        print('得分：' + str(len(result) * 2))
        obj = {
            'name':file,
            'sorce':str(len(result) * 2)
        }
        bigArr.append(obj)
        print(result)
    print(bigArr)
    DataFrame =pd.DataFrame(bigArr)
    #unData中创建summary文件夹
    if not os.path.isdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary'):
        os.mkdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary')
    DataFrame.to_excel("D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary\\result5_2.xlsx",index=None,sheet_name='每种作品得分',header=["作品号","得分"])
    print(DataFrame)
