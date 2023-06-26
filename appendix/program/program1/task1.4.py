import fitz, time, re, os

def pdf2pic(pdfPath, picPath,filename):
    t = time.process_time()
    findXO = r"/Type(?= */XObject)"
    findIM = r"/Subtype(?= */Image)"

    # 打开pdf
    readData = fitz.open(pdfPath)
    # 图片计数
    imgNum = 0
    xreLen = readData.xref_length()

    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(pdfPath, len(readData), xreLen - 1))

    # 遍历每一个对象
    for i in range(1, xreLen):
        # 定义对象字符串
        Text = readData.xref_object(i)
        isXObject = re.search(findXO, Text)
        isImage = re.search(findIM, Text)
        if not isXObject or not isImage:
            continue
        imgNum += 1
        pix = fitz.Pixmap(readData, i)
        newName = filename + "_{}.png".format(imgNum)
        newName = newName.replace(':', '')

        # pix.n<5,直接存为PNG
        if pix.n < 5:
            pix.save(os.path.join(picPath, newName))
        # 否则转换CMYK
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(picPath, newName))
            pix0 = None
        pix = None
        t1 = time.process_time()
        print("运行时间:{}s".format(t1 - t))
        print("提取了{}张图片".format(imgNum))


if __name__ == '__main__':
    path = 'D:\\桌面\\泰迪杯数据分析A题\\unDataA'
    file_list = os.listdir(path)
    filename = "task2_3.pdf"

    for files in file_list:
        #pdf路径
        pdfPath = r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\'+files+'\\task2_3.pdf'
        picPath = r'D:\\桌面\\泰迪杯数据分析A题\\unDataA\\'+files+'\\image'
        filelist = os.listdir("D:\\桌面\\泰迪杯数据分析A题\\unDataA\\"+files)
        #遍历查找是否有目标PDF文件
        for file2 in filelist:
            if filename in file2:
                m = pdf2pic(pdfPath, picPath,files)
            else:
                print(files+"内没有task2_3.pdf")