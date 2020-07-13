#coding=utf8
import os
import xlrd
from common.excel_utilts import ExcelUtiles

excel_path =os.path.join(os.path.dirname(__file__),'data/stu_data.xlsx')
excelUtils = ExcelUtiles(excel_path,"Sheet1")
# print(excelUtils.get_merged_cell_value02(6,0))

#获取表格数据
sheet_list = []
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    row_dict["事件"] = excelUtils.get_merged_cell_value02(row,0)
    row_dict["步骤序号"] = excelUtils.get_merged_cell_value02(row, 1)
    row_dict["步骤操作"] = excelUtils.get_merged_cell_value02(row, 2)
    row_dict["完成情况"] = excelUtils.get_merged_cell_value02(row, 3)
    sheet_list.append(row_dict)
#遍历取所有数据
# for row in sheet_list:
#     print(row)


#方法二（使用遍历的方式获取表格数据）：
all_data_list = []
first_row = excelUtils.sheet.row(0)
# print(first_row)
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0,excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value02(row,col)
    all_data_list.append(row_dict)

for row in all_data_list:
    print(row)