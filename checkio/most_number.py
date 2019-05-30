def most_number(*args):
    if not args:
        return 0
    else:
        return max(args) - min(args)


print(most_number(1, 2, 3))
print(most_number(5, -5))
print(most_number(10.2, -2.2, 0, 1.1, 0.5))
