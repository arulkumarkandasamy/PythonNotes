def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def reverse_slice(string):
   string = string[::-1]
   return string
s = "Geeksforgeeks"

print ("The original string  is : ")
print (s)

print ("The reversed string(using loops) is : ")
print (reverse_slice(s))