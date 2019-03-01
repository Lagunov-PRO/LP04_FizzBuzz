for number in range(1, 101):
    f = 'Fizz' if number % 3 == 0 else ''
    b = 'Buzz' if number % 5 == 0 else ''
    fizzbuzz = ('{}{}'.format(f, b))
    print(number if not fizzbuzz else fizzbuzz)
