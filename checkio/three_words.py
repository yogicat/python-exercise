def three_words(text):
    count = 0
    for word in text.split():
        if word.isalpha():
            count += 1
        else:
            count = 0

        if count >= 3:
            return True
    return False


print(three_words('Hello World Hello'))
print(three_words('Hello World 3'))
print(three_words('he is 123 man'))
print(three_words('1 2 3 4 '))
