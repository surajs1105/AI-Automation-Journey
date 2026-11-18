def character_frequency(text):
    for ch in text:
        print(ch, ":", text.count(ch))


character_frequency("hello")