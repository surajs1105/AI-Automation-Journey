# Check whether two strings are anagrams using dictionaries.
str1 = "listen"
str2 = "silent"

frequency1 = {}
frequency2 = {}

for char in str1:
    frequency1[char] = frequency1.get(char, 0) + 1

for char in str2:
    frequency2[char] = frequency2.get(char, 0) + 1

if frequency1 == frequency2:
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")