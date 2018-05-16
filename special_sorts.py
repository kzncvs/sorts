import xlsxwriter
import generate
import datetime
import tools
import sys
import threading

RUNS_COUNT = 20
data_types = ['byte', 'int', 'string', 'date']
data_volumes = [5, 50, 500, 5000]
generation_types = ['straight']
generated_arrays = []


def quick_sort_iterative(list_, left, right):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left, right))

    # Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))


def quick_sort_recursive(list_, left, right):
    """
    Quick sort method (Recursive)
    """
    if right <= left:
        return
    else:
        # Get pivot
        piv = partition(list_, left, right)
        # Sort left side of pivot
        quick_sort_recursive(list_, left, piv - 1)
        # Sort right side of pivot
        quick_sort_recursive(list_, piv + 1, right)


def partition(list_, left, right):
    """
    Partition method
    """
    # Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right

    while 1:
        while i <= j and list_[i] <= piv:
            i += 1
        while j >= i and list_[j] >= piv:
            j -= 1
        if j <= i:
            break
        # Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    # Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j



def merge(a, left, mid, right):
    """
    Merge fuction
    """
    # Copy array
    copy_list = []
    i, j = int(left), int(mid + 1)
    ind = left

    while ind < right + 1:

        # if left array finish merging, copy from right side
        if i > mid:
            copy_list.append(a[int(j)])
            j += 1
        # if right array finish merging, copy from left side
        elif j > right:
            copy_list.append(a[i])
            i += 1
        # Check if right array value is less than left one
        elif a[j] < a[i]:
            copy_list.append(a[j])
            j += 1
        else:
            copy_list.append(a[i])
            i += 1
        ind += 1

    ind = 0
    for x in (range(int(left), int(right + 1))):
        a[x] = copy_list[ind]
        ind += 1


def merge_sort(list_, left, right):
    """
    MergeSort Recursive Method
    """
    if len(list_) is 0:
        return
    # Stop condition for the recursion
    if right <= left:
        return
    else:
        mid = (right + left) / 2  # Middle point
        merge_sort(list_, left, mid)  # Sort left half
        merge_sort(list_, mid + 1, right)  # Sort right half
        merge(list_, left, mid, right)  # Merge left and right sides


def merge_sort_iterative(list_, left, right):
    """
    Iterative version of the Merge Sort Algorithm
    """
    factor = 2
    temp_mid = 0
    # Main loop to iterate over the array by 2^n.
    while 1:
        index = 0
        left = 0
        right = len(list_) - (len(list_) % factor) - 1
        mid = (factor / 2) - 1

        # Auxiliary array to merge subdivisions
        while index < right:
            temp_left = index
            temp_right = temp_left + factor - 1
            mid2 = (temp_right + temp_left) / 2
            merge(list_, temp_left, mid2, temp_right)
            index = (index + factor)

        # Chek if there is something to merge from the remaining
        # Sub-array created by the factor
        if len(list_) % factor and temp_mid != 0:
            # merge sub array to later be merged to the final array
            merge(list_, right + 1, temp_mid, len(list_) - 1)
            # Update the pivot
            mid = right
        # Increase the factor
        factor = factor * 2
        temp_mid = right

        # Final merge, merge subarrays created by the subdivision
        # of the factor to the main array.
        if factor > len(list_):
            mid = right
            right = len(list_) - 1
            merge(list_, 0, mid, right)
            break


def generate_arrays():
    start_time = datetime.datetime.now()
    for i in range(RUNS_COUNT):
        new_arr = {}
        for generation_type in generation_types:
            new_gen_type = {}
            for data_volume in data_volumes:
                new_vol = {}
                for data_type in data_types:
                    print("generating", i, generation_type, data_volume, data_type)
                    new_vol.update({data_type: generate.make_me(generation_type, data_volume, data_type)})
                new_gen_type.update({data_volume: new_vol})
            new_arr.update({generation_type: new_gen_type})
        generated_arrays.append(new_arr)
    finish_time = datetime.datetime.now()
    print("generated in", finish_time - start_time)


def make():
    sort_type = 'quick_sort_recursive'
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
                    target_array = generated_arrays[run][generation_type][data_volume][data_type]
                    print(sort_type, generation_type, data_volume, data_type, run)
                    start_time = datetime.datetime.now()
                    quick_sort_recursive(target_array, 0, data_volume - 1)
                    finish_time = datetime.datetime.now()
                    runs_times.append(finish_time - start_time)
                average = tools.time_average(runs_times)
                worksheet.write(j + 1, i + 1, average)

    sort_type = 'quick_sort_iterative'
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
                    target_array = generated_arrays[run][generation_type][data_volume][data_type]
                    print(sort_type, generation_type, data_volume, data_type, run)
                    start_time = datetime.datetime.now()
                    quick_sort_iterative(target_array, 0, data_volume - 1)
                    finish_time = datetime.datetime.now()
                    runs_times.append(finish_time - start_time)
                average = tools.time_average(runs_times)
                worksheet.write(j + 1, i + 1, average)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    generate_arrays()
    thread = threading.Thread(target=make)
    thread.start()
