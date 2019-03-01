def fizzbuzz(substitutes={'Fizz': 3, 'Buzz': 5}, upper_limit=100):
    """
    Replaces the numbers divisible by 3 with Fizz, by 5 with Buzz, with both by FizzBuzz and so on...
    >>> fizzbuzz({'Fizz': 3, 'Buzz': 5}, 20)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']

    >>> fizzbuzz({'Fizz': 3, 'Buzz': 5, 'Fuzz': 7}, 200)[100:110]
    [101, 'Fizz', 103, 104, 'FizzBuzzFuzz', 106, 107, 'Fizz', 109, 'Buzz']
    """
    result = []
    for number in range(1, upper_limit + 1):
        replacement = ''
        for substitute, divisor in substitutes.items():
            replacement += substitute if number % divisor == 0 else ''
            number_or_replacement = number if not replacement else replacement
        result.append(number_or_replacement)
    return result

