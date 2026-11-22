# DSA 4: List searching vs dictionary lookup (average-case complexity)
#   List search       : O(n) - may scan every element
#   Dictionary lookup : O(1) average - hash gives the location directly
import time

n = 200_000
data_list = list(range(n))
data_dict = {i: True for i in range(n)}
target = n - 1   # worst case for the list

start = time.perf_counter()
for _ in range(100):
    target in data_list
list_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(100):
    target in data_dict
dict_time = time.perf_counter() - start

print(f"List search (100 runs)       : {list_time:.6f} s")
print(f"Dictionary lookup (100 runs) : {dict_time:.6f} s")
print(f"Dictionary is ~{list_time / dict_time:.0f}x faster here")
