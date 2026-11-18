# Check Palindrome or not 
def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("madam"))
print(is_palindrome("python"))