from collections import OrderedDict

def getCharCountDict(string):
    h=OrderedDict()
    for i in string:
        if i in h:
            h[i] += 1;
        else:
            h[i] = 1
    return h

def firstNonRepeatingChar(string):
    h=getCharCountDict(string)
    print (h)
    index = -1
    k = 0
    for i in string:
        if h[i] == 1:
            index = k
            break
        k+=1

    return index

string = "geeksforgeeks"
index = firstNonRepeatingChar(string)
if index==1:
   print ("Either all characters are repeating or string is empty")
else:
   print ("First non-repeating character is " + string[index])