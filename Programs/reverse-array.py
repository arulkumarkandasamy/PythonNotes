def reverse_array(arr):
    size = len(arr)
    hiIndex = size-1
    its_req = size/2

    for i in range(0,int(its_req)):
        temp = arr[hiIndex]
        arr[hiIndex] = arr[i]
        arr[i] = temp
        hiIndex -= 1

    print("Done!")

array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]

print(array)                    # Print the original sequence
reverse_array(array)        # Call the function passing the list
print (array)                    # Print reversed list