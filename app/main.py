for number in range(1, 101):
    # if number % 3 == 0 and number % 5 == 0:
    #     print('FizzBuzz')
    if number % 3 == 0:
        print('Fizz', end='' if number % 5 == 0 else '\n')
    if number % 5 == 0:
        print('Buzz')
    else:
        print(number)
