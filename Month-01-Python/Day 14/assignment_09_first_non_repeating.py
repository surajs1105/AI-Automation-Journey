text = "swiss"

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

answer = None
for ch in text:
    if freq[ch] == 1:
        answer = ch
        break

print(answer)   # w
