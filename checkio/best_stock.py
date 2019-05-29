def best_stock(data):
    # solution 1.
    # max = 0
    # res = ''
    # for k in data:
    #     if data[k] > max:
    #         max = data[k]
    #         res = k

    # solution 2.
    # for key in data:
    #     if data[key] == max(data.values()):
    #         return key

    # solution 3.
    return max(data, key=lambda item: data[item])


assert best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}) == 'ATX', "First"
assert best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
}) == 'TASI', "Second"
print("Coding complete.")
