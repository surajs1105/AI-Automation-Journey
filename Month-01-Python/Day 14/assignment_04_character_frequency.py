def char_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

text = input("Enter a string: ")
for ch, count in char_frequency(text).items():
    print(ch, count)
