numbers = [5, 15, 25, 35, 45, 55, 65]

target = 45

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Element found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")