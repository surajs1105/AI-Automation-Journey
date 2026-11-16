# Count pairs with equal value in [1, 2, 2, 3, 3, 3]
nums = [1, 2, 2, 3, 3, 3]
count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count)   # 4