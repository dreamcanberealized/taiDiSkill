#导入OS模块
import os

#待搜索的名称
filename1 = "task2_1.xlsx"
filename2 = "task2_2.xlsx"
filename3 = "task2_3.pdf"
filename4 = "task3.xlsx"

#定义保存结果的数组
theresult = []

def findfiles(path):
    # 首先遍历当前目录所有文件及文件夹
    the_file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for file in the_file_list:
    	# 利用os.path.join()方法取得路径全名，并存入curpath变量，否则每次只能遍历一层目录
        curpath = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(curpath):
            findfiles(curpath)
        else:
        	# 判断是否是特定文件名称
            if filename1 in file:
                theresult.append(file)
            elif filename2 in file:
                theresult.append(file)
            elif filename3 in file:
                theresult.append(file)
            elif filename4 in file:
                theresult.append(file)



if __name__ == '__main__':
    path = 'D:\\桌面\\泰迪杯数据分析A题\\unDataA'
    fileList = os.listdir(path)
    #unDataA中创建summary文件夹 task1.2
    if not os.path.isdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\summary'):
        os.mkdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\summary')
    #遍历文件夹文件并在每个文件夹下创建image文件夹 task1.2
    for file in fileList:
        if not os.path.isdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\'+file+'\image'):
            os.mkdir(r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\'+file+'\image')
    # 遍历文件夹文件并寻找对应文件 task1.3
    for file in fileList:
        theresult = []
        findfiles(path + '\\' + file)
        print(file + '的得分为：' + str(len(theresult) * 2))
        print(theresult)