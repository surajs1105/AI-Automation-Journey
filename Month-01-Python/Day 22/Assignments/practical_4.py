# Practical 4: Handle FileNotFoundError using try-except
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return None


with open("exists.txt", "w") as f:
    f.write("This file exists.\n")

print(read_file("exists.txt"))
print(read_file("missing_file.txt"))
