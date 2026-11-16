# Common elements between [10, 20, 30, 40] and [20, 40, 50]
a = [10, 20, 30, 40]
b = [20, 40, 50]
common = []

for x in a:
    for y in b:
        if x == y:
            common.append(x)

print(common)   # [20, 40]