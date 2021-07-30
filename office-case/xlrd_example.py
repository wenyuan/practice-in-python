#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用第三方库：pip install xlrd xlwt xlutils
一般用于处理老版本 Excel(.xls)
"""

import xlwt
import xlrd
from xlutils.copy import copy


# 写入 Excel
def write_excel():
    # 创建 xls 文件对象
    workbook = xlwt.Workbook()

    # 新增两个表单页
    sheet_1 = workbook.add_sheet('成绩')
    sheet_2 = workbook.add_sheet('汇总')

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一个 sheet
    sheet_1.write(0, 0, '姓名')
    sheet_1.write(0, 1, '专业')
    sheet_1.write(0, 2, '科目')
    sheet_1.write(0, 3, '成绩')

    sheet_1.write(1, 0, '张三')
    sheet_1.write(1, 1, '信息与通信工程')
    sheet_1.write(1, 2, '数值分析')
    sheet_1.write(1, 3, 88)

    sheet_1.write(2, 0, '李四')
    sheet_1.write(2, 1, '物联网工程')
    sheet_1.write(2, 2, '数字信号处理分析')
    sheet_1.write(2, 3, 95)

    sheet_1.write(3, 0, '王华')
    sheet_1.write(3, 1, '电子与通信工程')
    sheet_1.write(3, 2, '模糊数学')
    sheet_1.write(3, 3, 90)

    # 写入第二个 sheet
    sheet_2.write(0, 0, '总分')
    sheet_2.write(1, 0, 273)

    # 最后保存文件即可
    workbook.save('student.xls')


# 读取 Excel
def read_excel():
    # 打开刚才我们写入的 student.xls 文件
    workbook = xlrd.open_workbook("student.xls")

    # 获取并打印 sheet 数量
    print("sheet 数量:", workbook.nsheets)

    # 获取并打印 sheet 名称
    print("sheet 名称:", workbook.sheet_names())

    # 根据 sheet 索引获取内容
    sheet_1 = workbook.sheet_by_index(0)
    # 或者
    # 也可根据 sheet 名称获取内容
    # sh = workbook.sheet_by_name('成绩')

    # 获取并打印该 sheet 行数和列数
    print("sheet %s 共 %d 行 %d 列" % (sheet_1.name, sheet_1.nrows, sheet_1.ncols))

    # 获取并打印某个单元格的值
    print("第一行第二列的值为:", sheet_1.cell_value(0, 1))

    # 获取整行或整列的值
    rows = sheet_1.row_values(0)  # 获取第一行内容
    cols = sheet_1.col_values(1)  # 获取第二列内容

    # 打印获取的行列值
    print("第一行的值为:", rows)
    print("第二列的值为:", cols)

    # 获取单元格内容的数据类型
    print("第二行第一列的值类型为:", sheet_1.cell(1, 0).ctype)

    # 遍历所有表单内容
    for sh in workbook.sheets():
        for r in range(sh.nrows):
            # 输出指定行
            print(sh.row(r))


# 修改 Excel
def edit_excel():
    # 打开刚才我们写入的 student.xls 文件
    workbook = xlrd.open_workbook("student.xls")

    # 复制一份
    new_workbook = copy(workbook)

    # 选取第一个表单
    sheet_1 = new_workbook.get_sheet(0)

    # 在第五行新增写入数据
    sheet_1.write(4, 0, '王欢')
    sheet_1.write(4, 1, '通信工程')
    sheet_1.write(4, 2, '机器学习')
    sheet_1.write(4, 3, 89)

    # 选取第二个表单
    sheet_2 = new_workbook.get_sheet(1)

    # 替换总成绩数据
    sheet_2.write(1, 0, 362)

    # 保存
    new_workbook.save('new_student.xls')


# 格式化 Excel
def format_excel():
    # 设置写出格式字体红色加粗
    style_head = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

    # 设置数字型格式为小数点后保留两位
    style_num = xlwt.easyxf(num_format_str='#,##0.00')

    # 设置日期型格式显示为YYYY-MM-DD
    style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD')

    # 创建 xls 文件对象
    workbook = xlwt.Workbook()

    # 新增两个表单页
    sheet_1 = workbook.add_sheet('成绩')
    sheet_2 = workbook.add_sheet('汇总')

    # 然后按照位置来添加数据，第一个参数是行，第二个参数是列
    sheet_1.write(0, 0, '姓名', style_head)  # 设置表头字体为红色加粗
    sheet_1.write(0, 1, '日期', style_head)  # 设置表头字体为红色加粗
    sheet_1.write(0, 2, '成绩', style_head)  # 设置表头字体为红色加粗

    # 插入数据
    sheet_1.write(1, 0, '张三', )
    sheet_1.write(1, 1, '2021-07-01', style_date)
    sheet_1.write(1, 2, 90, style_num)
    sheet_1.write(2, 0, '李四')
    sheet_1.write(2, 1, '2021-08-02')
    sheet_1.write(2, 2, 95, style_num)

    # 设置单元格内容居中的格式
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    style = xlwt.XFStyle()
    style.alignment = alignment

    # 合并 A4，B4 单元格，并将内容设置为居中
    sheet_1.write_merge(3, 3, 0, 1, '总分', style)

    # 通过公式，计算 C2+C3 单元格的和
    sheet_1.write(3, 2, xlwt.Formula("C2+C3"))

    # 对 sheet2 写入数据
    sheet_2.write(0, 0, '总分', style_head)
    sheet_2.write(1, 0, 185)

    # 最后保存文件即可
    workbook.save('student.xls')


if __name__ == "__main__":
    # write_excel()
    # read_excel()
    # edit_excel()
    format_excel()
