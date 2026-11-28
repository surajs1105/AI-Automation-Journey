# Day 22 - Writing data into a file ("w" mode overwrites existing content)
file = open("demo.txt", "w")
file.write("Welcome to ASCEND 365")
file.close()                      # always close with the basic open() approach

print("demo.txt written")
