def missing_numbers(num_list):
    original_list = [x for x in range(num_list[0],num_list[-1]+1)]
    return (list(set(num_list) ^ set(original_list)))

print(missing_numbers([1,2,4,6,7,10]))