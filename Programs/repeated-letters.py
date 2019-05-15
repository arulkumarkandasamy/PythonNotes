def count_repeated_letters(string1):
    list1 = []

    for letter in string1:
        if string1.count(letter) >= 2:
            if letter not in list1:
                list1.append(letter)

    for item in list1:
        if item != "":
            print(item,string1.count(item))

count_repeated_letters('letter has 1 e and 2 e and 1 t and two t')
