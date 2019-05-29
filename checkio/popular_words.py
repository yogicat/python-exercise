def popular_words(text, words):
    res = {}
    text_list = text.lower().split()

    # solution 1
    # for word in words:
    #     res[word] = text_list.count(word)
    # return res

    # solution 2
    # same but in comprehension.
    return {word: text_list.count(word) for word in words}


print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
