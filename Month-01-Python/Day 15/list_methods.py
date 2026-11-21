# Python list methods - examples in a single program

fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1. append() - add one item at the end
fruits.append("mango")
print("append('mango'):", fruits)

# 2. insert() - add an item at a given index
fruits.insert(1, "orange")
print("insert(1, 'orange'):", fruits)

# 3. extend() - add many items at the end
fruits.extend(["grape", "kiwi"])
print("extend(['grape', 'kiwi']):", fruits)

# 4. remove() - remove the first matching value
fruits.remove("banana")
print("remove('banana'):", fruits)

# 5. pop() - remove and return item (last item by default)
last = fruits.pop()
print("pop() removed:", last, "->", fruits)
second = fruits.pop(1)
print("pop(1) removed:", second, "->", fruits)

# 6. index() - position of the first matching value
print("index('cherry'):", fruits.index("cherry"))

# 7. count() - how many times a value appears
nums = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print("\nNumbers:", nums)
print("count(1):", nums.count(1))

# 8. sort() - sort the list in place
nums.sort()
print("sort():", nums)
nums.sort(reverse=True)
print("sort(reverse=True):", nums)

# 9. reverse() - reverse the list in place
nums.reverse()
print("reverse():", nums)

# 10. copy() - make a separate copy
backup = nums.copy()
print("copy():", backup)

# 11. clear() - remove all items
backup.clear()
print("clear():", backup)

# Handy built-in functions that work with lists
print("\nlen:", len(nums))
print("min:", min(nums))
print("max:", max(nums))
print("sum:", sum(nums))
print("sorted (new list):", sorted(nums))