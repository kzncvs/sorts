def time_aver(time_arr):
    kek = 0
    for time in time_arr:
        kek += time.total_seconds()
    return kek / len(time_arr)
