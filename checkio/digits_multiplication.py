def digits_multiplication(number):
    result = 1
    for i in str(number):
        if int(i):
            result *= int(i)
    return result


print(digits_multiplication(123405))
print(digits_multiplication(999))
