import glob
import os
import gzip
import tarfile
import zipfile
import rarfile
import time
import py7zr

def undataA():
    # 解压DataA
    if not os.path.isdir("D:\\桌面\\泰迪杯数据分析A题\\DataA"):
        os.mkdir("D:\\桌面\\泰迪杯数据分析A题\\DataA")
    # 放置DataA解压缩文件
    if not os.path.isdir("D:\\桌面\\泰迪杯数据分析A题\\unDataA"):
        os.mkdir("D:\\桌面\\泰迪杯数据分析A题\\unDataA")

    path_rar = "D:\\桌面\\泰迪杯数据分析A题\\DataA.rar"

    path_folder = "D:\\桌面\\泰迪杯数据分析A题\\DataA"

    temp = rarfile.RarFile(path_rar)  # 待解压文件

    temp.extractall(path_folder)
# 解压DataA
# undataA()
# 解压缩子文件夹



def unzip(filename):
    suffix = filename.split('.')[0]
    print(suffix)

    path_rar = "D:\\桌面\\泰迪杯数据分析A题\\DataA\\" + filename
    path_folder = "D:\\桌面\\泰迪杯数据分析A题\\unDataA\\" + suffix

    print("path_rar",path_rar)
    print("path_folder",path_folder)

    zip_file = zipfile.ZipFile(path_rar)
    if not os.path.isdir(path_folder):
        os.mkdir(path_folder)
    for names in zip_file.namelist():
        zip_file.extract(names, path_folder)
    zip_file.close()

def unrar(filename):
    suffix = filename.split('.')[0]
    print(suffix)
    # if (suffix == A221)
    path_rar = "D:\\桌面\\泰迪杯数据分析A题\\DataA\\" + filename
    path_folder = "D:\\桌面\\泰迪杯数据分析A题\\unDataA\\" + suffix

    print("path_rar",path_rar)
    print("path_folder",path_folder)

    if not os.path.isdir(path_folder):
        os.mkdir(path_folder)

    temp = rarfile.RarFile(path_rar)  # 待解压文件
    temp.extractall(path_folder)  # 解压文件夹
    temp.close()

def un7z(filename):
    suffix = filename.split('.')[0]
    print(suffix)

    path_rar = "D:\\桌面\\泰迪杯数据分析A题\\DataA\\" + filename
    path_folder = "D:\\桌面\\泰迪杯数据分析A题\\unDataA\\" + suffix

    print("path_rar",path_rar)
    print("path_folder",path_folder)

    with py7zr.SevenZipFile(path_rar, mode='r') as z:
        z.extractall(path_folder)

def un_files(filename_lst):
    print("filename_lst",filename_lst)
    print('for:')
    for filename in filename_lst:
        print('for',filename)
        if '.' in filename:
            suffix = filename.split('.')[-1]
            if suffix == 'zip':
                unzip(filename)
                # os.remove(filename)
            if suffix == 'rar':
                unrar(filename)
                # os.remove(filename)
            if suffix == '7z':
                un7z(filename)
                # os.remove(filename)

path = r'D:\桌面\泰迪杯数据分析A题\DataA'
file_lst = glob.glob(path + '/*')
filename_lst = [os.path.basename(i) for i in file_lst]
un_files(filename_lst);


