# import xlrd
# excel = xlrd.open_workbook('../data/data.xlsx')
# #指定工作表，通过名字定位
# sheet = excel.sheet_by_name('添加卡')
# #通过第0个
# sheet = excel.sheet_by_index(0)

# print(sheet.nrows)#有效数据行数
# print(sheet.ncols)#有效数据列数
#
# print(sheet.row_values(0))#打印第一行数据
# print(sheet.row_values(1))#打印第一行数据
#
# print(sheet.cell(1,0).value)#打印指定单元格数据

#遍历注册表两条数据

# for a in range(1,sheet.nrows):
#     print(sheet.row_values(a))


import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(0,2,'性别')
book.save('stu.xls')






