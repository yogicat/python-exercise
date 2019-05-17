def digits_multiplication(number):
    arr = [int(i) for i in str(number)]
    result = 1
    for i in arr:
        if i != 0:
            result = result * i
    return result


print(digits_multiplication(123405))
