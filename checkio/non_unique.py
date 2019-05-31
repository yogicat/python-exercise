def non_unique(data):
    # res = []
    # for item in data:
    #     if data.count(item) >= 2:
    #         res.append(item)
    # return res

    return [a for a in data if data.count(a) > 1]


print(non_unique([1, 2, 3, 1, 3]))
print(non_unique([1, 2, 3, 4, 5]))
