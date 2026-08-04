"""
devmath.arithmetic
Basic arithmetic functions.
"""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a % b


def power(a, b):
    return a ** b


def square(n):
    return n * n


def cube(n):
    return n * n * n


def sqrt(n):
    if n < 0:
        raise ValueError("Square root of negative number is not supported.")
    return math.sqrt(n)


def cube_root(n):
    if n >= 0:
        return n ** (1 / 3)
    return -((-n) ** (1 / 3))


def absolute(n):
    return abs(n)


def reciprocal(n):
    if n == 0:
        raise ZeroDivisionError("Zero has no reciprocal.")
    return 1 / n


def percentage(part, total):
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")
    return (part / total) * 100


def percentage_of(percent, number):
    return (percent / 100) * number


def increase_by_percent(value, percent):
    return value + percentage_of(percent, value)


def decrease_by_percent(value, percent):
    return value - percentage_of(percent, value)


def average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty.")
    return sum(numbers) / len(numbers)


def summation(numbers):
    return sum(numbers)


def product(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def maximum(numbers):
    return max(numbers)


def minimum(numbers):
    return min(numbers)


def clamp(value, minimum_value, maximum_value):
    return max(minimum_value, min(value, maximum_value))


def round_number(number, digits=0):
    return round(number, digits)


def ceil(number):
    return math.ceil(number)


def floor(number):
    return math.floor(number)


def remainder(a, b):
    return math.remainder(a, b)


def log(number, base=10):
    return math.log(number, base)


def ln(number):
    return math.log(number)


def log2(number):
    return math.log2(number)


def log10(number):
    return math.log10(number)


def exp(number):
    return math.exp(number)