for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print('{}{}'.format('Fizz' if number % 3 == 0 else '', 'Buzz' if number % 5 == 0 else ''))
    else:
        print(number)
