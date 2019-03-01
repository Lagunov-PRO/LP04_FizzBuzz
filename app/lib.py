def fizzbuzz(upper_limit: int, f, b):
    """
    >>> fizzbuzz(20, 3, 5)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
    """
    result = []
    for number in range(1, upper_limit + 1):
        substitute = ''
        substitute += 'Fizz' if number % f == 0 else ''
        substitute += 'Buzz' if number % b == 0 else ''
        number_or_substitute = number if not substitute else substitute
        result.append(number_or_substitute)
    return result