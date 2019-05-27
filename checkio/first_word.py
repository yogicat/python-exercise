def first_word(text):
    return text.replace('.', ' ').replace(',', ' ').strip().split()[0]


print(first_word('Hello, world.'))
