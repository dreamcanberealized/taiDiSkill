#导入模块
import os
import pandas as pd

#待搜索的名称
filename1 = "task2_1.xlsx"
filename2 = "task2_2.xlsx"
filename3 = "task2_3.pdf"
filename4 = "task3.xlsx"

result = []  #定义保存结果的数组
groupname = '' #文件名暂存
# 信息数组
task5_5Arr = []

def findfiles(path):
    print(os.listdir(path))
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    fileMsg = []
    for file in file_list:
    	# 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        print(cur_path)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            findfiles(cur_path)
        else:
        	# 判断是否是特定文件名称
            if filename1 in file:
                obj = {
                    'groupName':groupname,
                    'filename':filename1,
                    'path':cur_path
                }
                settask5_5Arr(obj)

                # result.append(file)
            elif filename2 in file:
                obj = {
                    'groupName': groupname,
                    'filename':filename2,
                    'path':cur_path
                }
                settask5_5Arr(obj)

                # result.append(file)
            elif filename3 in file:
                obj = {
                    'groupName': groupname,
                    'filename':filename3,
                    'path':cur_path
                }
                settask5_5Arr(obj)

                # result.append(file)
            elif filename4 in file:
                obj = {
                    'groupName': groupname,
                    'filename':filename4,
                    'path':cur_path
                }
                fileMsg.append(obj)

                # result.append(file)
    print(fileMsg)

    return fileMsg



def settask5_5Arr(fileMsg):
    print('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print("fileArr",fileMsg)
    print(groupname)
    task5_5Arr.append(fileMsg)
    print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

if __name__ == '__main__':
    path = 'D:\\桌面\\泰迪杯数据分析A题\\unDataB'
    file_list = os.listdir(path)
    print(file_list)
    # 遍历文件夹文件并寻找对应文件
    for file in file_list:
        result = []
        print(file)
        groupname = file
        fileArr = findfiles(path + '\\' + file)

    DataFrame = pd.DataFrame(task5_5Arr)
    excel_path = r"D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary\\result5_3_1.xlsx"
    DataFrame.to_excel(excel_path,index=None,sheet_name='每种作品得分',header=["作品号","文件名","路径"])
    print(DataFrame)
