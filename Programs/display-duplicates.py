def display_duplicates(numlist):
    size = len(numlist)
    duplicate = []
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if numlist[i] == numlist[j] and numlist[i] not in duplicate:
                duplicate.append(numlist[i])

    return duplicate

list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
#print (Repeat(list1))
print(display_duplicates(list1))