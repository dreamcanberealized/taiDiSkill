"""
任务 2.3 读取每份作品“task2_3.pdf”中产品登记数量及排名的表格，针对
每个排名判断“分组标签”和“产品登记数量”的数值与表 2 中的标准答案是否
一致，每个匹配的数值得 2 分，满分 12 分。
"""
import os
import  pandas as pd
import pdfplumber

d= {
    '排名':["分组标签","产品登记数量"],
    '一':[7,2012],
    '二':[6,1501],
    '三':[5,1038]
}
frame = pd.DataFrame(d,index=[0,1])

res = {}
def read(left,right):
    for i in range(left,right):
        name = "dataA/A" + str(i) + "/task2_3.pdf"
        s=0
        if os.path.exists(name):
            pdf = pdfplumber.open(name)
            ps = pdf.pages
            #第四页
            for k in range(len(ps)):
                pg = ps[k]
                tables = pg.extract_tables()
                if tables == []:
                    continue
                table = tables[0]

                df = pd.DataFrame(table[1:], columns=table[0])
                #拿出表格
                for i in range(len(table)):
                    for j in range(len(table[i])):
                        table[i][j] = table[i][j].replace('\n', '')
                df1 = pd.DataFrame(table[1:], columns=table[0])
                df1_col = str(df1.columns.values)
                if "排名" not in df1_col:
                    continue
                df1_biaoqian_1 = str(df1.loc[0]["一"])
                df1_biaoqian_2 = str(df1.loc[0]["二"])
                df1_biaoqian_3 = str(df1.loc[0]["三"])

                df2_biaoqian_1 = str(df1.loc[1]["一"])
                df2_biaoqian_2 = str(df1.loc[1]["二"])
                df3_biaoqian_3 = str(df1.loc[1]["三"])

                frame_1 = str(frame.loc[0]["一"])
                frame_2= str(frame.loc[0]["二"])
                frame_3 = str(frame.loc[0]["三"])

                frame1_1 = str(frame.loc[1]["一"])
                frame1_2 =str (frame.loc[1]["二"])
                frame1_3 = str(frame.loc[1]["三"])

                if df1_biaoqian_1 == frame_1:
                    s+=2
                if df1_biaoqian_2 == frame_2:
                    s += 2
                if df1_biaoqian_3 == frame_3:
                    s += 2
                if df2_biaoqian_1 == frame1_1:
                    s += 2
                if df2_biaoqian_2 == frame1_2:
                    s += 2
                if df3_biaoqian_3 == frame1_3:
                    s += 2
                break
            res[name]=s
        print(name+"分数为:"+str(s))
if __name__ == '__main__':
    read(101,420)

