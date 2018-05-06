import xlsxwriter
import sorts
import generate
from multiprocessing.dummy import Pool as ThreadPool
import datetime
import sys
import threading


def xlsx_generator():
    data_types = ['byte', 'int', 'string', 'date']
    data_volumes = [5, 50, 500, 5000, 50000, 500000]

    workbook = xlsxwriter.Workbook('python.xlsx')
    worksheet_straight = workbook.add_worksheet('straight')
    worksheet_reverse = workbook.add_worksheet('reverse')
    worksheet_sorted = workbook.add_worksheet('sorted')
    for i in range(len(data_volumes)):
        worksheet_straight.write(0, i + 1, data_volumes[i])
        worksheet_reverse.write(0, i + 1, data_volumes[i])
        worksheet_sorted.write(i + 1, 0, data_types[i])
    for i in range(len(data_types)):
        worksheet_straight.write(i + 1, 0, data_types[i])
        worksheet_reverse.write(i + 1, 0, data_types[i])
        worksheet_sorted.write(i + 1, 0, data_types[i])

    def time_aver(time_arr):
        kek = 0
        for time in time_arr:
            kek += time.total_seconds()
        return kek / len(time_arr)

    def sort_time_straight(hop):
        arr = generate.make_array(data_vo, data_ty)
        print("computing ", data_vo, " ", data_ty, " ", hop)
        start_time = datetime.datetime.now()
        sorts.python(arr)
        finish_time = datetime.datetime.now()
        return finish_time - start_time

    def sort_time_reversed(hop):
        arr = generate.make_reverse(data_vo, data_ty)
        print("computing ", data_vo, " ", data_ty, " ", hop)
        start_time = datetime.datetime.now()
        sorts.python(arr)
        finish_time = datetime.datetime.now()
        return finish_time - start_time

    def sort_time_sorted(hop):
        arr = generate.make_sorted(data_vo, data_ty)
        print("computing ", data_vo, " ", data_ty, " ", hop)
        start_time = datetime.datetime.now()
        sorts.python(arr)
        finish_time = datetime.datetime.now()
        return finish_time - start_time

    for i in range(len(data_volumes)):
        for j in range(len(data_types)):
            data_ty = data_types[j]
            data_vo = data_volumes[i]
            pool = ThreadPool(4)
            results = pool.map(sort_time_straight, range(0, 4))
            average = time_aver(results)
            worksheet_straight.write(j + 1, i + 1, average)

            results = pool.map(sort_time_reversed, range(0, 4))
            average = time_aver(results)
            worksheet_reverse.write(j + 1, i + 1, average)

            results = pool.map(sort_time_sorted, range(0, 4))
            average = time_aver(results)
            worksheet_sorted.write(j + 1, i + 1, average)

    workbook.close()


if __name__ == '__main__':
    xlsx_generator()
