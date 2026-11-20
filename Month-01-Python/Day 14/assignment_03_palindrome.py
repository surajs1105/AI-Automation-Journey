def is_palindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

word = input("Enter a string: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
