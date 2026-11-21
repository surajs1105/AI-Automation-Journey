stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek
print("Top element:", stack[-1])

# Pop
removed = stack.pop()

print("Removed:", removed)
print("Updated Stack:", stack)