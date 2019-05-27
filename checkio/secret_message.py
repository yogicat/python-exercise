def find_message(msg):
    # return ''.join(filter(str.isupper, msg))
    # return ''.join(filter(lambda s: s.isupper(), msg))
    return ''.join(s for s in msg if s.isupper())

print(find_message("Hello World Peace!"))
