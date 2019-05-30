def right_left(text):
    return ','.join(text).replace('right', 'left')


print(right_left(("left", "right", "left", "stop")))
print(right_left(("bright aright", "ok")))
print(right_left(("brightness wright",)))
print(right_left(("enough", "jokes")))
