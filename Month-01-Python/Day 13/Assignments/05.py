# Count the frequency of each word in a sentence.
sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)