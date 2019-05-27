def second_index(text, char):

    # find returns -1, index returns error

    # solution 1.
    # if text.count(char) < 2:
    #     return None
    # return text.find(char, text.find(char) + 1)

    # return text.find(char, text.find(char) + 1) if text.count(char) > 1 else None

    # solution 2.
    try:
        return text.index(char, text.index(char) + 1)
    except ValueError:
        return None


print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", " "))
