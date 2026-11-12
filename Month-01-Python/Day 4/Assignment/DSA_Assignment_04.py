numbers = [10, 20, 30, 40, 50]
target = 40

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Target {target} found at index {i}")
        break
    