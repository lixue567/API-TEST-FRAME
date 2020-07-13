#coding=utf8

import os
import xlrd

class ExcelUtiles():
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()    #整个表格对象

    #封装获取表格
    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    #封装获取所有行
    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    # 封装获取列
    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    #获取所有数据
    def __get_cell_value(self,row_index,col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    #获取所有合并单元格
    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value02(self,row_index, col_index):
        """既能完成获取普通单元格的数据又能获取合并单元格数据"""
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value(rlow, clow)
                    break;  # 防止循环去进行判断出现值覆盖的情况
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)
            else:
                cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_data_by_dict(self):
        all_data_list = []
        first_row = self.sheet.row(0)   #获取首行数据
        for row in range(1, excelUtils.get_row_count()):
            row_dict = {}
            for col in range(0, excelUtils.get_col_count()):
                row_dict[first_row[col].value] = excelUtils.get_merged_cell_value02(row, col)
            all_data_list.append(row_dict)
        return all_data_list


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path,'..','samples/data/test_data.xlsx')
    excelUtils = ExcelUtiles(excel_path,"Sheet1")
    for row in excelUtils.get_sheet_data_by_dict():
        print( row)