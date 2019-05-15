import sys

def print2Smallest(arr):
    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid input")
        return

    first = second = 999999

    for i in range (0, arr_size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif (arr[i] < second and second != first):
            second = arr[i]

    if (second == 999999):
        print("No second smallest element")
    else:
        print('The smallest element is', first, 'and' \
                                          ' second smallest element is', second)


arr = [12, 13, 1, 10, 34, 3]
print2Smallest(arr)