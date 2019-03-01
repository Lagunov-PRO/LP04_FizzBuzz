def fizzbuzz(upper_limit: int, substitutes: dict):
    """
    >>> fizzbuzz(20, {'Fizz' : 3, 'Buzz' : 5})
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
    """
    result = []
    for number in range(1, upper_limit + 1):
        replacement = ''
        for substitute, divisor in substitutes.items():
            replacement += substitute if number % divisor == 0 else ''
            number_or_replacement = number if not replacement else replacement
        result.append(number_or_replacement)
    return result

