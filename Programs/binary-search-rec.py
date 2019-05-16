def binary_search_rec(arr, item):
    def _binary_search(item, first, last, arr):
        if last < first:
            return False
        if last == first:
            # return arr[last] == item
            return last
        mid = (first + last) // 2
        if arr[mid] > item:
            last = mid
            return _binary_search(item, first, last, arr)
        elif arr[mid] < item:
            first = mid + 1
            return _binary_search(item, first, last, arr)
        else:
            #return arr[mid] == item
            return mid

    return _binary_search(item, 0, len(arr) - 1, arr)


print(binary_search_rec([1,5,8,10,20,50,60,70,80],60))