def is_empty(stack):
    return len(stack) == 0

stack = []
print("Empty stack:", is_empty(stack))       # True

stack.append(10)
print("After push:", is_empty(stack))        # False

stack.pop()
print("After pop:", is_empty(stack))         # True
