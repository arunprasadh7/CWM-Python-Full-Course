# Fizz buzz problem

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        message = 'Fizz Buzz'
    elif number % 3 == 0:
        message = 'Fizz'
    elif number % 5 == 0:
        message = 'Buzz'
    else:
        message = number
    return message


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print(fizz_buzz(21))
print('--------------------------------------------------------')

# method 2

def fizzbizz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return 'Fizz Bizz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Bizz'
    return number

print(fizzbizz(3))
print(fizzbizz(5))
print(fizzbizz(15))
print(fizzbizz(30))
print(fizzbizz(7))