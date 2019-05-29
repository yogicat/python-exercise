def fizz_buzz(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return str(number)


print(fizz_buzz(15))
print(fizz_buzz(6))
print(fizz_buzz(5))
print(fizz_buzz(7))
