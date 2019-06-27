#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
import os
from xlutils.copy import copy


# excel基类
class BaseExcel(object):
    def __init__(self, filename, sheetid=0):
        self.filename = filename
        self.sheetid = sheetid
        self.data = xlrd.open_workbook(self.filename)
        self.table = self.data.sheet_by_index(self.sheetid)


# excel读操作
class ReadExcel(BaseExcel):
    # 获取所有的行数
    def get_lines(self):
        return self.table.nrows

    # 获取所有的数据
    def get_data(self):
        rows = self.get_lines()
        data = []
        for i in range(1, rows):
            data.append(self.table.row_values(i))
        return data

    # 获取某一行的数据
    def get_row_data(self, row_index):
        """
        :param row_index:   行号
        :return:
        """
        return self.table.row_values(row_index)

    # 获取单元格的数据
    def get_cell_data(self, row_index, col_index):
        return self.table.cell_value(row_index, col_index)


# excel写操作
# 写入新文件，以免污染测试源
class WriteExcel(BaseExcel):
    def __init__(self, filepath, sheetid=0):
        super().__init__(filepath, sheetid)
        self.new_file = self.copy_file()
        self.new_data = xlrd.open_workbook(self.new_file, formatting_info=True)
        self.new_table = self.new_data.sheet_by_index(self.sheetid)
        self.raw_data = copy(self.new_data)   # 将新文件的内容读到内存
        self.raw_table = self.raw_data.get_sheet(0)  # 读取内存中的sheet

    # 复制一份新文件
    def copy_file(self):
        file_dir = os.path.dirname(self.filename)  # 文件目录
        file_basename = os.path.basename(self.filename)  # 原文件名
        name, postfix = file_basename.split('.')
        filename = name + '_new.' + postfix   # 新文件名
        new_file = os.path.join(file_dir, filename)  # 新文件的完整路径
        data = copy(self.data)
        data.save(new_file)
        return new_file

    # 写入内存
    def write(self, row, col, value):
        self.raw_table.write(row, col, value)

    # 从内存写入新文件
    def sava(self):
        self.raw_data.save(self.new_file)


# if __name__ == '__main__':
#     e = ReadExcel('../data/case1.xls')
#     print(e.get_row_data(1))
#     print(e.get_cell_data(1, 2))
#
#     w = WriteExcel('../data/case1.xls')
#     w.write(3, 11, 'failed')
#     w.write(4, 11, 'pass')
#     w.sava()

