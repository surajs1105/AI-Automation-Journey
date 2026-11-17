def common_elements(a, b):
    common = []
    for x in a:
        if x in b and x not in common:
            common.append(x)
    return common

print(common_elements([10, 20, 30, 40], [20, 40, 50]))   # [20, 40]