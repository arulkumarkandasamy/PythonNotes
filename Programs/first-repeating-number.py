def first_repeating_number(numlist):
    h = {}
    for i in numlist:
        if i in h:
            return i
        else:
            h[i] = 0

    return 0;

numlist = [1,2,5,7,5,3,9,0]
print (first_repeating_number(numlist))




