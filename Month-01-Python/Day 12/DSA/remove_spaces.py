def remove_spaces(text):
    result = ""

    for ch in text:
        if ch != " ":
            result += ch

    return result


print(remove_spaces("I love Python"))