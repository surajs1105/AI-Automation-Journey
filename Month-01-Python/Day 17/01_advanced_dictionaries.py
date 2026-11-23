# Day 17 - Python: Advanced Dictionary Operations

# 3.1 update()
student = {"name": "Amit", "marks": 75}
student.update({"marks": 90, "branch": "Computer"})
print(student)

# 3.2 get(key, default)
student = {"name": "Rahul", "marks": 85}
print(student.get("name"))
print(student.get("age", 20))

# 3.3 setdefault()
student = {"name": "Amit"}
result = student.setdefault("marks", 0)
print(result)
print(student)

# 3.4 Merging with |  (right-hand side wins on overlapping keys)
a = {"name": "Suraj", "age": 24}
b = {"branch": "Computer", "age": 25}
c = a | b
print(c)
