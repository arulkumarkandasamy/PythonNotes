def getNumCountDict(numlist):
    h = {}
    for i in numlist:
        if i in h:
            h[i] += 1;
        else:
            h[i] = 1
    return h

def getNonRepeatingNumber(numlist):
    h=getNumCountDict(numlist)

    for i in numlist:
        if h[i] == 1:
            return i

    return 0

numlist = [1,1,2,2,5,7,5,3,9,4,8]
print (getNonRepeatingNumber(numlist))



