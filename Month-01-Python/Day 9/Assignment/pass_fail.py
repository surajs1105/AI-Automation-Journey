def result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print(result(75))   # Pass
print(result(40))   # Pass
print(result(35))   # Fail