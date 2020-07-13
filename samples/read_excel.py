#coding=utf8
import os
import xlrd

excel_path =os.path.join(os.path.dirname(__file__),'data/stu_data.xlsx')
# print(excel_path)

wb = xlrd.open_workbook(excel_path)  #创建工作薄对象
sheet = wb.sheet_by_name("Sheet1")   #创建表格对象（方法一）
# sheet = wb.sheet_by_index(0)  #获取单元格（方法二）
cell_value = sheet.cell_value(0,0)
print(cell_value)
cell_value = sheet.cell_value(1,0)
print(cell_value)
cell_value = sheet.cell_value(2,0)  #对于合并的左上角首个单元格会返回真实值
print(cell_value)

#利用xlrd处理合并单元格
# print(sheet.merged_cells)   #获取当前表格中所有合并的单元格，返回一个列表   起始行，结束行，起始列，结束列
merged = sheet.merged_cells

#逻辑：凡是在merged_cells属性范围内的单元格，它的值都要等于左上角首个单元格的值
row_index = 3;col_index = 0

for(rlow,rhigh,clow,chigh) in merged:  #遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh):  #行坐标判断   1<=3<5
        if (col_index >= clow and col_index < chigh): #列坐标   0<=0<1
            # 如果满足条件，就把合并单元格第一个位置的值赋给其他合并单元格
            cell_value = sheet.cell_value(rlow,clow)
print(cell_value)

#封装
def get_merged_cell_value01(row_index,col_index):
    """"只能完成获取合并单元格的数据"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
    return cell_value
print(get_merged_cell_value01(4,0))
print("......................")
def get_merged_cell_value02(row_index,col_index):
    """既能完成获取普通单元格的数据又能获取合并单元格数据"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                break; #防止循环去进行判断出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index,col_index)
        else:
            cell_value = sheet.cell_value(row_index,col_index)
    return cell_value

print(get_merged_cell_value02(4, 0))

for i in range(1,9):
    print(get_merged_cell_value02(i, 3))
print(sheet.merged_cells)