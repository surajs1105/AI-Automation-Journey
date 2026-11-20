a = [10, 20, 30, 40]
b = [20, 40, 50, 60]

common = []
for x in a:
    if x in b and x not in common:
        common.append(x)

print(common)   # [20, 40]
