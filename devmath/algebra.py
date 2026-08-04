"""
devmath.algebra
Algebra functions and equation solvers.
"""

import math
import cmath


# ======================
# LINEAR EQUATIONS
# ======================

def solve_linear(a, b):
    """
    Solve ax + b = 0
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    return -b / a


# ======================
# QUADRATIC EQUATIONS
# ======================

def discriminant(a, b, c):
    """
    Return the discriminant (b² - 4ac)
    """
    return b**2 - 4*a*c


def solve_quadratic(a, b, c):
    """
    Solve ax² + bx + c = 0
    Returns real or complex roots.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")

    d = discriminant(a, b, c)

    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
    else:
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)

    return root1, root2


# ======================
# POLYNOMIALS
# ======================

def polynomial(coefficients, x):
    """
    Evaluate polynomial.
    Example:
    coefficients=[2,3,1]
    Returns 2x² + 3x + 1
    """
    result = 0
    degree = len(coefficients) - 1

    for coef in coefficients:
        result += coef * (x ** degree)
        degree -= 1

    return result


# ======================
# SEQUENCES
# ======================

def arithmetic_nth_term(a, d, n):
    """
    nth term of Arithmetic Progression
    """
    return a + (n - 1) * d


def arithmetic_sum(a, d, n):
    """
    Sum of Arithmetic Progression
    """
    return n * (2*a + (n - 1)*d) / 2


def geometric_nth_term(a, r, n):
    """
    nth term of Geometric Progression
    """
    return a * (r ** (n - 1))


def geometric_sum(a, r, n):
    """
    Sum of Geometric Progression
    """
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)


# ======================
# BINOMIAL
# ======================

def binomial_coefficient(n, r):
    """
    nCr
    """
    return math.comb(n, r)


# ======================
# COMPLEX NUMBERS
# ======================

def complex_add(z1, z2):
    return z1 + z2


def complex_subtract(z1, z2):
    return z1 - z2


def complex_multiply(z1, z2):
    return z1 * z2


def complex_divide(z1, z2):
    return z1 / z2


def complex_modulus(z):
    return abs(z)


def complex_argument(z):
    return cmath.phase(z)


def complex_conjugate(z):
    return z.conjugate()


# ======================
# VECTORS (2D)
# ======================

def vector_add(v1, v2):
    return (
        v1[0] + v2[0],
        v1[1] + v2[1]
    )


def vector_subtract(v1, v2):
    return (
        v1[0] - v2[0],
        v1[1] - v2[1]
    )


def dot_product(v1, v2):
    return (
        v1[0] * v2[0] +
        v1[1] * v2[1]
    )


def vector_magnitude(v):
    return math.sqrt(
        v[0]**2 + v[1]**2
    )


def unit_vector(v):
    mag = vector_magnitude(v)

    if mag == 0:
        raise ValueError("Zero vector has no direction.")

    return (
        v[0] / mag,
        v[1] / mag
    )


def angle_between_vectors(v1, v2):
    dot = dot_product(v1, v2)

    mag = (
        vector_magnitude(v1) *
        vector_magnitude(v2)
    )

    return math.degrees(
        math.acos(dot / mag)
    )


# ======================
# EXPANSIONS
# ======================

def square_identity(a, b):
    """
    (a+b)^2
    """
    return a**2 + 2*a*b + b**2


def cube_identity(a, b):
    """
    (a+b)^3
    """
    return (
        a**3 +
        3*a*a*b +
        3*a*b*b +
        b**3
    )


# ======================
# MISC
# ======================

def distance_on_number_line(a, b):
    return abs(a - b)


def ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b