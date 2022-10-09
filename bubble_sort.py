'''
bubble sorting
get the size of the array
set a while loop that checks the array size is larger than zero (for every successful for loop, reduce size by 1
because after first loop and subsequent loops, the largest numbers will be sorted permanently)
for loop between 0 and the size of the array-1 (as you cannot check the last array value against nothing)
    swapping adjacent values if a is larger than b
original = O(N^2)

improvement:
if no swapping as occured, break loop

'''


def bubble_sorting(array):
    n = len(array)

    while n > 0:
        swapped = False
        for i in range(0, n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            print(n)
            break
        n -= 1
    return array


array_test = [100, 0, 4, 2, 6, 8, 2, 4, 11, 10]

print(bubble_sorting(array_test))
