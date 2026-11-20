numbers = [12, 45, 23, 67, 34, 67, 10]

largest = None
second = None

for n in numbers:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif n != largest and (second is None or n > second):
        second = n

print("Second largest:", second)   # 45
