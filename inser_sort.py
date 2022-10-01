'''
Insert Sort
'''


def insert_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


unsort_array = [9, 7, 4, 5, 45, 6, 1, 3]
sorted_array = insert_sort(unsort_array)
print(sorted_array)
