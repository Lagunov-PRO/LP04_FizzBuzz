for number in range(1, 101):
    fizzbuzz = ''
    fizzbuzz += 'Fizz' if number % 3 == 0 else ''
    fizzbuzz += 'Buzz' if number % 5 == 0 else ''
    result = number if not fizzbuzz else fizzbuzz
    print(result)

