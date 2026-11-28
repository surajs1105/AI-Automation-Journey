# Python 5: Append new information without deleting existing content
with open("log.txt", "w") as f:               # start with some content
    f.write("First entry\n")

with open("log.txt", "a") as file:            # "a" keeps what is already there
    file.write("Second entry (appended)\n")
    file.write("Third entry (appended)\n")

with open("log.txt", "r") as file:
    print(file.read())
