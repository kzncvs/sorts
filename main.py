import xlsxwriter
import sorts
import generate

data_types = ['byte', 'int', 'string', 'date']
data_volumes = [50, 500, 5000, 50000, 500000]

workbook = xlsxwriter.Workbook('bubble.xlsx')
worksheet = workbook.add_worksheet('straight')
for i in range(len(data_volumes)):
    worksheet.write(0, i + 1, data_volumes[i])
for i in range(len(data_types)):
    worksheet.write(i + 1, 0, data_types[i])

