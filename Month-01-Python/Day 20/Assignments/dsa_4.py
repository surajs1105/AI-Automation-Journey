# DSA 4: Second-highest mark in a list


def second_highest(marks):
    """Returns the second-highest DISTINCT mark, or None."""
    highest = second = None
    for m in marks:                      # single pass, O(n)
        if highest is None or m > highest:
            second = highest
            highest = m
        elif m != highest and (second is None or m > second):
            second = m
    return second


marks = [75, 90, 85, 65, 90, 78]
print("Marks:", marks)
print("Second highest:", second_highest(marks))              # 85 (duplicates of 90 ignored)

# Alternative: sort distinct values
print("Using sorted+set:", sorted(set(marks), reverse=True)[1])
print("Single value list:", second_highest([50, 50]))        # None
