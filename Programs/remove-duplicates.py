def remove_duplicates(duplist):
    final_list = []

    for num in duplist:
        if num not in final_list:
            final_list.append(num)

    return final_list

# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
#print(Remove(duplicate))
print(remove_duplicates(duplicate))
