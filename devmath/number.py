"""
devmath.number
Number theory and utility functions.
"""

import math


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_positive(n):
    return n > 0


def is_negative(n):
    return n < 0


def is_zero(n):
    return n == 0


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def previous_prime(n):
    n -= 1
    while n > 1:
        if is_prime(n):
            return n
        n -= 1
    return None


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    if n > 2:
        factors.append(n)

    return factors


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed.")
    return math.factorial(n)


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative.")

    sequence = []

    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def nth_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative.")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))


def digit_count(n):
    return len(str(abs(n)))


def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)

    total = sum(int(d) ** power for d in digits)

    return total == abs(n)


def is_perfect(n):
    if n <= 1:
        return False

    total = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total == n


def is_perfect_square(n):
    if n < 0:
        return False
    return int(math.sqrt(n)) ** 2 == n


def is_perfect_cube(n):
    cube = round(abs(n) ** (1 / 3))
    return cube ** 3 == abs(n)


def is_multiple(a, b):
    if b == 0:
        return False
    return a % b == 0


def is_divisible(a, b):
    if b == 0:
        return False
    return a % b == 0


def divisors(n):
    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)

            if i != n // i:
                result.append(n // i)

    return sorted(result)


def count_divisors(n):
    return len(divisors(n))


def sum_divisors(n):
    return sum(divisors(n))


def coprime(a, b):
    return math.gcd(a, b) == 1


def triangular_number(n):
    return n * (n + 1) // 2


def is_triangular(n):
    x = 8 * n + 1
    return int(math.sqrt(x)) ** 2 == x


def catalan(n):
    return math.factorial(2 * n) // (
        math.factorial(n + 1) * math.factorial(n)
    )


def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)


def combinations(n, r):
    return math.factorial(n) // (
        math.factorial(r) * math.factorial(n - r)
    )


def decimal_to_binary(n):
    return bin(n)[2:]


def decimal_to_octal(n):
    return oct(n)[2:]


def decimal_to_hexadecimal(n):
    return hex(n)[2:].upper()


def binary_to_decimal(binary):
    return int(binary, 2)


def octal_to_decimal(octal):
    return int(octal, 8)


def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)