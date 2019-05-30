def absolute_sorting(list):

    return tuple(sorted(list, key=abs))


print(absolute_sorting([-5, 10, -20, 3]))
