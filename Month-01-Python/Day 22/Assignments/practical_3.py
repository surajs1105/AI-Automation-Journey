# Practical 3: Use with open() instead of manually closing files

# Manual approach (risky: if write() raises an error, close() is never reached)
file = open("compare.txt", "w")
file.write("manual close\n")
file.close()

# Recommended approach
with open("compare.txt", "w") as file:
    file.write("with open() - closed automatically\n")

print("Is the file closed after the with block?", file.closed)   # True

with open("compare.txt", "r") as file:
    print(file.read())
