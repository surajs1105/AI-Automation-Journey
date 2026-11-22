# Python 4: Frequency of each character in a string using a dictionary
text = input("Enter a string: ") if False else "hello world"   # change as needed

frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch, count in frequency.items():
    print(f"'{ch}' : {count}")
