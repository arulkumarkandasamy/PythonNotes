```
Arrays

We can treat lists as arrays. However, we cannot constraint the type of elements stored in a list. For example:

a = [1, 3.5, "Hello"]

If you create arrays using array module, all elements of the array must be of the same numeric type.

import array as arr

a = arr.array('d', [1, 3.5, "Hello"])   // Error

How to create arrays?

As you might have guessed from the above example, we need to import array module to create arrays. For example:

import array as arr

a = arr.array('d', [1.1, 3.5, 4.5])

print(a)

Here, we created an array of float type. The letter 'd' is a type code. This determines the type of the array during creation.

How to access array elements?

We use index to access elements of an array:

import array as arr

a = arr.array('i', [2, 4, 6, 8])



print("First element:", a[0])

print("Second element:", a[1])

print("Second last element:", a[-1])

How to slice arrays?

We can access a range of items in an array by using the slicing operator :.

import array as arr



numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]

numbers_array = arr.array('i', numbers_list)



print(numbers_array[2:5]) # 3rd to 5th

print(numbers_array[:-5]) # beginning to 4th

print(numbers_array[5:])  # 6th to end

print(numbers_array[:])   # beginning to end

When you run the program, the output will be:

array('i', [62, 5, 42])

array('i', [2, 5, 62])

array('i', [52, 48, 5])

array('i', [2, 5, 62, 5, 42, 52, 48, 5])

How to change or add elements?

Arrays are mutable; their elements can be changed in a similar way like lists.

import array as arr



numbers = arr.array('i', [1, 2, 3, 5, 7, 10])



# changing first element

numbers[0] = 0

print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])



# changing 3rd to 5th element

numbers[2:5] = arr.array('i', [4, 6, 8])

print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

We can add one item to a list using append() method or add several items using extend() method.

import array as arr



numbers = arr.array('i', [1, 2, 3])



numbers.append(4)

print(numbers)     # Output: array('i', [1, 2, 3, 4])



# extend() appends iterable to the end of the array

numbers.extend([5, 6, 7])

print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

We can concatenate two arrays using + operator.

import array as arr



odd = arr.array('i', [1, 3, 5])

even = arr.array('i', [2, 4, 6])



numbers = arr.array('i')   # creating empty array of integer

numbers = odd + even



print(numbers)

How to remove/delete elements?

We can delete one or more items from an array using del statement.

import array as arr



number = arr.array('i', [1, 2, 3, 3, 4])



del number[2] # removing third element

print(number) # Output: array('i', [1, 2, 3, 4])



del number # deleting entire array

print(number) # Error: array is not defined

We can use remove() method to remove the given item or pop() method to remove an item at the given index.

import array as arr



numbers = arr.array('i', [10, 11, 12, 12, 13])



numbers.remove(12)

print(numbers)   # Output: array('i', [10, 11, 12, 13])



print(numbers.pop(2))   # Output: 12

print(numbers)   # Output: array('i', [10, 11, 13])

Check this page to learn more about Python array and array methods:

When to use arrays?

Lists are much more flexible than arrays. They can store elements of different data types including string. Also, lists are faster than arrays. And, if you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy library.





Lists

How to create a list?

In Python programming, a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.).

# empty list

my_list = []



# list of integers

my_list = [1, 2, 3]



# list with mixed datatypes

my_list = [1, "Hello", 3.4]

Also, a list can even have another list as an item. This is called nested list.

# nested list

my_list = ["mouse", [8, 4, 6], ['a']]

How to access elements from a list?

There are various ways in which we can access the elements of a list.

List Index

We can use the index operator [] to access an item in a list. Index starts from 0. So, a list having 5 elements will have index from 0 to 4.

Trying to access an element other that this will raise an IndexError. The index must be an integer. We can't use float or other types, this will result into TypeError.

Nested list are accessed using nested indexing.

y_list = ['p','r','o','b','e']

# Output: p

print(my_list[0])

# Output: o

print(my_list[2])

# Output: e

Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

my_list = ['p','r','o','b','e']

# Output: e

print(my_list[-1])

# Output: p

print(my_list[-5])

How to slice lists in Python?

We can access a range of items in a list by using the slicing operator (colon).

my_list = ['p','r','o','g','r','a','m','i','z']

# elements 3rd to 5th

print(my_list[2:5])

# elements beginning to 4th

print(my_list[:-5])

# elements 6th to end

print(my_list[5:])

# elements beginning to end

print(my_list[:])

How to change or add elements to a list?

List are mutable, meaning, their elements can be changed unlike string or tuple.

We can use assignment operator (=) to change an item or a range of items.

# mistake values

odd = [2, 4, 6, 8]

# change the 1st item

odd[0] = 1

# Output: [1, 4, 6, 8]

print(odd)

# change 2nd to 4th items

odd[1:4] = [3, 5, 7]

# Output: [1, 3, 5, 7]

print(odd)

We can add one item to a list using append() method or add several items using extend() method.

odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]

print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]

print(odd)

We can also use + operator to combine two lists. This is also called concatenation.

The * operator repeats a list for the given number of times.

odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]

print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]

print(["re"] * 3)

Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

odd = [1, 9]

odd.insert(1,3)

# Output: [1, 3, 9]

print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]

print(odd)

How to delete or remove elements from a list?

We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

my_list = ['p','r','o','b','l','e','m']

# delete one item

del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']

print(my_list)

# delete multiple items

del my_list[1:5]

# Output: ['p', 'm']

print(my_list)

# delete entire list

del my_list

# Error: List not defined

print(my_list)

We can use remove() method to remove the given item or pop() method to remove an item at the given index.

The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).

We can also use the clear() method to empty a list.

my_list = ['p','r','o','b','l','e','m']

my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']

print(my_list)

# Output: 'o'

print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']

print(my_list)

# Output: 'm'

print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']

print(my_list)

my_list.clear()

# Output: []

print(my_list)

Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

>>> my_list = ['p','r','o','b','l','e','m']

>>> my_list[2:3] = []

>>> my_list

['p', 'r', 'b', 'l', 'e', 'm']

>>> my_list[2:5] = []

>>> my_list

['p', 'r', 'm']

Python List Methods

Python List Methods

append() - Add an element to the end of the list

extend() - Add all elements of a list to the another list

insert() - Insert an item at the defined index

remove() - Removes an item from the list

pop() - Removes and returns an element at the given index

clear() - Removes all items from the list

index() - Returns the index of the first matched item

count() - Returns the count of number of items passed as an argument

sort() - Sort items in a list in ascending order

reverse() - Reverse the order of items in the list

copy() - Returns a shallow copy of the list

Iterating Through a List

Using a for loop we can iterate though each item in a list.

for fruit in ['apple','banana','mango']:

    print("I like",fruit)

Built-in Functions with List

Function

Description

all()

Return True if all elements of the list are true (or if the list is empty).

any()

Return True if any element of the list is true. If the list is empty, return False.

enumerate()

Return an enumerate object. It contains the index and value of all the items of list as a tuple.

len()

Return the length (the number of items) in the list.

list()

Convert an iterable (tuple, string, set, dictionary) to a list.

max()

Return the largest item in the list.

min()

Return the smallest item in the list

sorted()

Return a new sorted list (does not sort the list itself).

sum()

Return the sum of all elements in the list.





List Comprehension

List comprehension is an elegant and concise way to create new list from an existing list in Python.

List comprehension consists of an expression followed by for statement inside square brackets.

Here is an example to make a list with each item being increasing power of 2.

pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

print(pow2)

This code is equivalent to

pow2 = []

for x in range(10):

   pow2.append(2 ** x)



While map maps a function over a sequence, list comprehensions map an expression over a sequence:

List Comprehension with filter

	[x for x in range(10) if x % 2 == 0]

	[(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]





Tuples

Creating a Tuple

A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma. The parentheses are optional but is a good practice to write it.

A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).

# empty tuple

# Output: ()

my_tuple = ()

print(my_tuple)



# tuple having integers

# Output: (1, 2, 3)

my_tuple = (1, 2, 3)

print(my_tuple)



# tuple with mixed datatypes

# Output: (1, "Hello", 3.4)

my_tuple = (1, "Hello", 3.4)

print(my_tuple)

# nested tuple

# Output: ("mouse", [8, 4, 6], (1, 2, 3))

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(my_tuple)

# tuple can be created without parentheses

# also called tuple packing

# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"

print(my_tuple)

# tuple unpacking is also possible

# Output:

# 3

# 4.6

# dog

a, b, c = my_tuple

print(a)

print(b)

print(c)

Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.

# only parentheses is not enough

# Output: <class 'str'>

my_tuple = ("hello")

print(type(my_tuple))

# need a comma at the end

# Output: <class 'tuple'>

my_tuple = ("hello",)

print(type(my_tuple))

# parentheses is optional

# Output: <class 'tuple'>

my_tuple = "hello",

print(type(my_tuple))

Accessing Elements in a Tuple

There are various ways in which we can access the elements of a tuple.

1. Indexing

We can use the index operator [] to access an item in a tuple where the index starts from 0.

So, a tuple having 6 elements will have index from 0 to 5. Trying to access an element other that (6, 7,...) will raise an IndexError.

The index must be an integer, so we cannot use float or other types. This will result into TypeError.

Likewise, nested tuple are accessed using nested indexing, as shown in the example below.

my_tuple = ('p','e','r','m','i','t')

# Output: 'p'

print(my_tuple[0])

# Output: 't'

print(my_tuple[5])

# index must be in range

# If you uncomment line 14,

# you will get an error.

# IndexError: list index out of range

#print(my_tuple[6])

# index must be an integer

# If you uncomment line 21,

# you will get an error.

# TypeError: list indices must be integers, not float

#my_tuple[2.0]

# nested tuple

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index

# Output: 's'

print(n_tuple[0][3])

# nested index

# Output: 4

print(n_tuple[1][1])



Named tuples (collections.namedtuple)

Point = collections.namedtuple('Point', ['x', 'y'])



Inheriting from named tuples





Set

How to create a set?

A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().

It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.

# set of integers

my_set = {1, 2, 3}

print(my_set)

# set of mixed datatypes

my_set = {1.0, "Hello", (1, 2, 3)}

print(my_set)

Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set() function without any argument.

# initialize a with {}

a = {}



# check data type of a

# Output: <class 'dict'>

print(type(a))



# initialize a with set()

a = set()



# check data type of a

# Output: <class 'set'>

print(type(a))

How to change a set in Python?

Sets are mutable. But since they are unordered, indexing have no meaning.

We cannot access or change an element of set using indexing or slicing. Set does not support it.

We can add single element using the add() method and multiple elements using the update() method. The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

# initialize my_set

my_set = {1,3}

print(my_set)



# if you uncomment line 9,

# you will get an error

# TypeError: 'set' object does not support indexing



#my_set[0]



# add an element

# Output: {1, 2, 3}

my_set.add(2)

print(my_set)



# add multiple elements

# Output: {1, 2, 3, 4}

my_set.update([2,3,4])

print(my_set)



# add list and set

# Output: {1, 2, 3, 4, 5, 6, 8}

my_set.update([4,5], {1,6,8})

print(my_set)

How to remove elements from a set?

A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.

The following example will illustrate this.

# initialize my_set

my_set = {1, 3, 4, 5, 6}

print(my_set)



# discard an element

# Output: {1, 3, 5, 6}

my_set.discard(4)

print(my_set)



# remove an element

# Output: {1, 3, 5}

my_set.remove(6)

print(my_set)



# discard an element

# not present in my_set

# Output: {1, 3, 5}

my_set.discard(2)

print(my_set)



# remove an element

# not present in my_set

# If you uncomment line 27,

# you will get an error.

# Output: KeyError: 2



#my_set.remove(2)

Similarly, we can remove and return an item using the pop() method.

Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.

We can also remove all items from a set using clear().

# initialize my_set

# Output: set of unique elements

my_set = set("HelloWorld")

print(my_set)



# pop an element

# Output: random element

print(my_set.pop())



# pop another element

# Output: random element

my_set.pop()

print(my_set)



# clear my_set

#Output: set()

my_set.clear()

print(my_set)

Python Set Operations

Set Union

# initialize A and B

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}



# use | operator

# Output: {1, 2, 3, 4, 5, 6, 7, 8}

print(A | B)



Set Intersection

# initialize A and B

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}



# use & operator

# Output: {4, 5}

print(A & B)



Set Difference

# initialize A and B

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}



# use - operator on A

# Output: {1, 2, 3}

print(A - B)



Set Symmetric Difference

# initialize A and B

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}



# use ^ operator

# Output: {1, 2, 3, 6, 7, 8}

print(A ^ B)

Different Python Set Methods

Method

Description

add()

Adds an element to the set

clear()

Removes all elements from the set

copy()

Returns a copy of the set

difference()

Returns the difference of two or more sets as a new set

difference_update()

Removes all elements of another set from this set

discard()

Removes an element from the set if it is a member. (Do nothing if the element is not in set)

intersection()

Returns the intersection of two sets as a new set

intersection_update()

Updates the set with the intersection of itself and another

isdisjoint()

Returns True if two sets have a null intersection

issubset()

Returns True if another set contains this set

issuperset()

Returns True if this set contains another set

pop()

Removes and returns an arbitary set element. Raise KeyError if the set is empty

remove()

Removes an element from the set. If the element is not a member, raise a KeyError

symmetric_difference()

Returns the symmetric difference of two sets as a new set

symmetric_difference_update()

Updates a set with the symmetric difference of itself and another

union()

Returns the union of sets in a new set

update()

Updates the set with the union of itself and others

Iterating Through a Set

for letter in set("apple"):

...     print(letter)

Built-in Functions with Set

Function

Description

all()

Return True if all elements of the set are true (or if the set is empty).

any()

Return True if any element of the set is true. If the set is empty, return False.

enumerate()

Return an enumerate object. It contains the index and value of all the items of set as a pair.

len()

Return the length (the number of items) in the set.

max()

Return the largest item in the set.

min()

Return the smallest item in the set.

sorted()

Return a new sorted list from elements in the set(does not sort the set itself).

sum()

Retrun the sum of all elements in the set.

Python Frozenset

Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the function frozenset().

This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.



Multisets and multiset operations (collections.Counter)



Dictionary

How to create a dictionary?

Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.

An item has a key and the corresponding value expressed as a pair, key: value.

While values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

# empty dictionary

my_dict = {}



# dictionary with integer keys

my_dict = {1: 'apple', 2: 'ball'}



# dictionary with mixed keys

my_dict = {'name': 'John', 1: [2, 4, 3]}



# using dict()

my_dict = dict({1:'apple', 2:'ball'})



# from sequence having each item as a pair

my_dict = dict([(1,'apple'), (2,'ball')])

As you can see above, we can also create a dictionary using the built-in function dict()

How to access elements from a dictionary?

While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method.

The difference while using get() is that it returns None instead of KeyError, if the key is not found.

my_dict = {'name':'Jack', 'age': 26}



# Output: Jack

print(my_dict['name'])



# Output: 26

print(my_dict.get('age'))



# Trying to access keys which doesn't exist throws error

# my_dict.get('address')

# my_dict['address']





How to change or add elements in a dictionary?

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.

If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.

my_dict = {'name':'Jack', 'age': 26}



# update value

my_dict['age'] = 27



#Output: {'age': 27, 'name': 'Jack'}

print(my_dict)



# add item

my_dict['address'] = 'Downtown'



# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}

print(my_dict)



How to delete or remove elements from a dictionary?

We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.

The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

# create a dictionary

squares = {1:1, 2:4, 3:9, 4:16, 5:25}



# remove a particular item

# Output: 16

print(squares.pop(4))



# Output: {1: 1, 2: 4, 3: 9, 5: 25}

print(squares)



# remove an arbitrary item

# Output: (1, 1)

print(squares.popitem())



# Output: {2: 4, 3: 9, 5: 25}

print(squares)



# delete a particular item

del squares[5]



# Output: {2: 4, 3: 9}

print(squares)



# remove all items

squares.clear()



# Output: {}

print(squares)



# delete the dictionary itself

del squares



# Throws Error

# print(squares)\



Python Dictionary Methods

Method

Description

clear()

Remove all items form the dictionary.

copy()

Return a shallow copy of the dictionary.

fromkeys(seq[, v])

Return a new dictionary with keys from seq and value equal to v (defaults to None).

get(key[,d])

Return the value of key. If key doesnot exit, return d (defaults to None).

items()

Return a new view of the dictionary's items (key, value).

keys()

Return a new view of the dictionary's keys.

pop(key[,d])

Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.

popitem()

Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.

setdefault(key[,d])

If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).

update([other])

Update the dictionary with the key/value pairs from other, overwriting existing keys.

values()

Return a new view of the dictionary's values





Here are a few example use of these methods.

marks = {}.fromkeys(['Math','English','Science'], 0)



# Output: {'English': 0, 'Math': 0, 'Science': 0}

print(marks)



for item in marks.items():

    print(item)



# Output: ['English', 'Math', 'Science']

list(sorted(marks.keys()))



Python Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.

Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.

Here is an example to make a dictionary with each item being a pair of a number and its square.

squares = {x: x*x for x in range(6)}



# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squares)

This code is equivalent to

squares = {}

for x in range(6):

   squares[x] = x*x



Here are some examples to make dictionary with only odd items.

odd_squares = {x: x*x for x in range(11) if x%2 == 1}



# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(odd_squares)



Dictionary comprehensions

m = {x: x ** 2 for x in range(5)}



Dictionary Comprehension

	D = { k:v for (k,v) in zip(keys, values)}

	D = {x: x**2 for x in [1,2,3,4,5]}



Iterating Through a Dictionary

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

for i in squares:

    print(squares[i])



Built-in Functions with Dictionary

Built-in functions like all(), any(), len(), cmp(), sorted() etc. are commonly used with dictionary to perform different tasks.

Function

Description

all()

Return True if all keys of the dictionary are true (or if the dictionary is empty).

any()

Return True if any key of the dictionary is true. If the dictionary is empty, return False.

len()

Return the length (the number of items) in the dictionary.

cmp()

Compares items of two dictionaries.

sorted()

Return a new sorted list of keys in the dictionary.





Ordered dictionaries (collections.OrderedDict)



Default dictionaries (collections.defaultdict)



Using default dictionaries to represent simple trees

```