foo = "SSYYNNOOPPSSIISSSI"


def rm_dup(input_str):
    final_list = []
    for c in foo:
        if c not in final_list:
            final_list.append(c)
    return ''.join(final_list)

print (rm_dup(foo))