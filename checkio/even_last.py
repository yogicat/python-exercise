def even_last(list):
    if not list:
        return 0

    return sum(list[::2]) * list[-1]


print(even_last([1, 3, 5]))
print(even_last([0, 1, 2, 3, 4, 5]))
print(even_last([6]))
print(even_last([]))
