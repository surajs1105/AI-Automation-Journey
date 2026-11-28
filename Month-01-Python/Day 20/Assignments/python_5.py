# Python 5: Compare sort() and sorted()
#
# | sort()                 | sorted()                  |
# |------------------------|---------------------------|
# | Modifies original list | Returns a new sorted list |
# | Returns None           | Returns the sorted list   |
# | List method            | Built-in function         |
# sorted() works on any iterable (tuple, set, string...); sort() only on lists.

numbers = [50, 20, 40, 10, 30]

new_list = sorted(numbers)
print("sorted() result :", new_list)
print("original list   :", numbers)        # unchanged

result = numbers.sort()
print("sort() returned :", result)         # None
print("original list   :", numbers)        # now sorted

# Common mistake:
# numbers = numbers.sort()   # would set numbers to None!

print("sorted on tuple :", sorted((3, 1, 2)))
print("sorted on string:", sorted("python"))
