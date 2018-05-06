import xlsxwriter
import sorts
import generate
import datetime
import tools


def xlsx_generator():
    data_types = ['byte', 'int', 'string', 'date']
    data_volumes = [5, 50, 500, 5000, 50000, 500000]
    sorting_types = ['bubble', 'heap', 'insertion', 'merge', 'quick', 'selection', 'shell', 'python']
    generation_types = ['straight', 'reversed', 'sorted', 'partly_sorted']
    RUNS_COUNT = 5

    for sort_type in sorting_types:
        workbook = xlsxwriter.Workbook('results/' + sort_type + '.xlsx')
        for generation_type in generation_types:
            worksheet = workbook.add_worksheet(generation_type)
            for i in range(len(data_volumes)):
                worksheet.write(0, i + 1, data_volumes[i])
                for j in range(len(data_types)):
                    worksheet.write(j + 1, 0, data_types[j])
                    data_volume = data_volumes[i]
                    data_type = data_types[j]
                    runs_times = []
                    for run in range(RUNS_COUNT):
                        target_array = generate.make_me(generation_type, data_volume, data_type)
                        print(sort_type, generation_type, data_volume, data_type, run)
                        start_time = datetime.datetime.now()
                        sorts.sort_me(sort_type, target_array)
                        finish_time = datetime.datetime.now()
                        runs_times.append(finish_time - start_time)
                    average = tools.time_average(runs_times)
                    worksheet.write(j + 1, i + 1, average)
        workbook.close()


if __name__ == '__main__':
    xlsx_generator()
