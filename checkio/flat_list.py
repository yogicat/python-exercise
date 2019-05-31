def flat_list(data):
    return sum(([x] if not isinstance(x, list) else flat_list(x) for x in data), [])


print(flat_list([1, [2, 2, 2], 4]))
