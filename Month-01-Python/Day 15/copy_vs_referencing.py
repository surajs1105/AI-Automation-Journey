
import copy

# 1. Referencing (b = a) - both names point to the SAME list

a = [1, 2, 3]
b = a
b.append(99)
print("1. Reference")
print("a:", a)                 # [1, 2, 3, 99]  <- a changed too!
print("b:", b)
print("Same object?", a is b)  # True


# 2. Shallow copy - a NEW list, independent for simple values
a = [1, 2, 3]
c = a.copy()                   # same as a[:] or list(a)
c.append(99)
print("\n2. Shallow copy")
print("a:", a)                 # [1, 2, 3]  <- unchanged
print("c:", c)
print("Same object?", a is c)  # False

# 3. Shallow copy problem with nested lists
x = [[1, 2], [3, 4]]
y = x.copy()
y[0].append(99)
print("\n3. Shallow copy with nested list")
print("x:", x)                 # [[1, 2, 99], [3, 4]]  <- x changed!
print("y:", y)

# 4. Deep copy - fully independent, even for nested lists
x = [[1, 2], [3, 4]]
z = copy.deepcopy(x)
z[0].append(99)
print("\n4. Deep copy")
print("x:", x)                 # [[1, 2], [3, 4]]  <- unchanged
print("z:", z)