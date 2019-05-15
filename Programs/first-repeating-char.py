def firstRepeatedChar(string):
    h = {}

    for ch in string:
        if ch in h:
            return ch
        else:
            h[ch]=0

    return 0

print(firstRepeatedChar("gegksforgeeks"))
