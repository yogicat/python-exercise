def index_power(arr, n):
    try:
        result = arr[n]**n
    except IndexError:
        result = -1

    return result


def index_power2(arr, n):
    return arr[n]**n if n < len(arr) else -1
