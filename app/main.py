for number in range(1, 101):
    fizzbuzz = ('{}{}'.format('Fizz' if number % 3 == 0 else '', 'Buzz' if number % 5 == 0 else ''))
    print(number if not fizzbuzz else fizzbuzz)
