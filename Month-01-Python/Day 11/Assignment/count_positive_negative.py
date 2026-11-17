def count_signs(nums):
    pos = neg = zero = 0
    for x in nums:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero

print(count_signs([3, -1, 0, 5, -7, 0]))  # (2, 2, 2)