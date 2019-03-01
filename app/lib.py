def fizzbuzz(substitutes={'Fizz': 3, 'Buzz': 5}, upper_limit=100):
    """
    Replaces the numbers divisible
        by 3 with Fizz
        by 5 with Buzz
        by both with FizzBuzz
        and so on...
    >>> fizzbuzz()[5:15]
    ['Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

    >>> fizzbuzz({'Fizz': 3, 'Buzz': 5, 'Fuzz': 7}, 200)[100:110]
    [101, 'Fizz', 103, 104, 'FizzBuzzFuzz', 106, 107, 'Fizz', 109, 'Buzz']
    """
    result = []
    for number in range(1, upper_limit + 1):
        substitution = ''
        for substitute, divisor in substitutes.items():
            substitution += substitute if number % divisor == 0 else ''
        result.append(number if not substitution else substitution)
    return result
