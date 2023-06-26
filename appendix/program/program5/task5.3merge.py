from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
import os
# 作品名单元格合并
def to_merge(df):
    # 按照第一列id进行每行单元格合并
    # id列去重，确定一列需要合并成几个值
    print(df)
    df_key = list(set(df['作品号'].values))
    wb = Workbook()
    ws = wb.active
    print("df_key",df_key)
    # 将每行数据写入ws中
    for row in dataframe_to_rows(df, index=False, header=True):
        # print(row)
        ws.append(row)
    #   遍历第一列去重后id
    for i in df_key:
        # 获取id等于指定值的几行数据
        print(i)
        print(df.loc[df["作品号"]==i, : ].index.tolist())
        df_id = df.loc[df["作品号"]==i, : ].index.tolist()  # 索引值从0开始
        for j in range(1, 2):  # 遍历 需要合并两列，openyxl中，读excel等的序号都是从1开始，所以合并两列，需要遍历range(1, 3)，取j=1,j=2
            ws.merge_cells(start_row=df_id[0] + 2, end_row=df_id[-1] + 2, start_column=j,
                           end_column=j)  # 序号从1开始，所以行序号需要加2

    excel_name = r"D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary\\result5_3.xlsx"
    # 保存writer中的数据至excel
    wb.save(excel_name)
    os.remove(r"D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary\\result5_3_1.xlsx")
    print('导入成功！')


df = pd.read_excel(r"D:\\桌面\\泰迪杯数据分析A题\\unDataB\\summary\\result5_3_1.xlsx", sheet_name=0)
to_merge(df)