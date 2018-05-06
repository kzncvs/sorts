def sort_me(sort, array):
    if sort == 'bubble':
        return bubble(array)
    elif sort == 'heap':
        return heap(array)
    elif sort == 'insertion':
        return insertion(array)
    elif sort == 'merge':
        return merge(array)
    elif sort == 'quick':
        return quick(array)
    elif sort == 'selection':
        return selection(array)
    elif sort == 'shell':
        return shell(array)
    elif sort == 'python':
        return python(array)


def bubble(array):
    if len(array) > 5000:
        return ' '
    exchanges = True
    pass_num = len(array) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                exchanges = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        pass_num = pass_num - 1
    return array


def heap(array):
    def move_down(array, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (array[largest] < array[largest + 1]):
                largest += 1

            # right child is larger than parent
            if array[largest] > array[first]:
                swap(array, largest, first)
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                return  # force exit

    def swap(a, x, y):
        tmp = a[x]
        a[x] = a[y]
        a[y] = tmp

    length = len(array) - 1
    least_parent = int(length / 2)
    for i in range(least_parent, -1, -1):
        move_down(array, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if array[0] > array[i]:
            swap(array, 0, i)
            move_down(array, 0, i - 1)

    return array


def insertion(array):
    if len(array) > 5000:
        return ' '
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = current_value
    return array


def merge(array):
    def __merge_sort(array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            __merge_sort(left_half)
            __merge_sort(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i = i + 1
                else:
                    array[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                array[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                array[k] = right_half[j]
                j = j + 1
                k = k + 1

    __merge_sort(array)
    return array


def quick(array):
    if len(array) > 5000:
        return ' '
    def partition(array, first, last):
        pivot_value = array[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and array[left_mark] <= pivot_value:
                left_mark = left_mark + 1
            while array[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark = right_mark - 1
            if right_mark < left_mark:
                done = True
            else:
                temp = array[left_mark]
                array[left_mark] = array[right_mark]
                array[right_mark] = temp

        temp = array[first]
        array[first] = array[right_mark]
        array[right_mark] = temp
        return right_mark

    def quick_sort_helper(array, first, last):
        if first < last:
            split_point = partition(array, first, last)
            quick_sort_helper(array, first, split_point - 1)
            quick_sort_helper(array, split_point + 1, last)

    quick_sort_helper(array, 0, len(array) - 1)

    return array


# def radix(array):
#     radix = 10
#     max_length = False
#     tmp, placement = -1, 1
#     while not max_length:
#         max_length = True
#         buckets = [list() for _ in range(radix)]
#         for i in array:
#             tmp = i / placement
#             buckets[int(tmp % radix)].append(i)
#             if max_length and tmp > 0:
#                 max_length = False
#         a = 0
#         for b in range(radix):
#             buck = buckets[b]
#             for i in buck:
#                 array[a] = i
#                 a += 1
#         placement *= radix
#     return array


def selection(array):
    if len(array) > 5000:
        return ' '
    for k in range(len(array) - 1):
        m = k
        i = k + 1
        while i < len(array):
            if array[i] < array[m]:
                m = i
            i += 1
        t = array[k]
        array[k] = array[m]
        array[m] = t
    return array


def shell(array):
    def __shell_sort(array):
        sublist_count = len(array) // 2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                gap_insertion_sort(array, start_position, sublist_count)
            sublist_count = sublist_count // 2

    def gap_insertion_sort(array, start, gap):
        for i in range(start + gap, len(array), gap):
            current_value = array[i]
            position = i
            while position >= gap and array[position - gap] > current_value:
                array[position] = array[position - gap]
                position = position - gap
            array[position] = current_value

    __shell_sort(array)
    return array


def python(array):
    array.sort()
    return array
