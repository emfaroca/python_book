def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

