"""
devmath.trigonometry
Trigonometric and angle functions.
"""

import math


# ==========================
# BASIC TRIGONOMETRIC FUNCTIONS
# ==========================

def sin(angle, degrees=True):
    """Return sine of an angle."""
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def cos(angle, degrees=True):
    """Return cosine of an angle."""
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)


def tan(angle, degrees=True):
    """Return tangent of an angle."""
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)


def cot(angle, degrees=True):
    """Return cotangent of an angle."""
    value = tan(angle, degrees)
    if value == 0:
        raise ZeroDivisionError("Cotangent is undefined.")
    return 1 / value


def sec(angle, degrees=True):
    """Return secant of an angle."""
    value = cos(angle, degrees)
    if value == 0:
        raise ZeroDivisionError("Secant is undefined.")
    return 1 / value


def cosec(angle, degrees=True):
    """Return cosecant of an angle."""
    value = sin(angle, degrees)
    if value == 0:
        raise ZeroDivisionError("Cosecant is undefined.")
    return 1 / value


# ==========================
# INVERSE TRIG FUNCTIONS
# ==========================

def asin(value, degrees=True):
    angle = math.asin(value)
    return math.degrees(angle) if degrees else angle


def acos(value, degrees=True):
    angle = math.acos(value)
    return math.degrees(angle) if degrees else angle


def atan(value, degrees=True):
    angle = math.atan(value)
    return math.degrees(angle) if degrees else angle


# ==========================
# HYPERBOLIC FUNCTIONS
# ==========================

def sinh(x):
    return math.sinh(x)


def cosh(x):
    return math.cosh(x)


def tanh(x):
    return math.tanh(x)


# ==========================
# ANGLE CONVERSIONS
# ==========================

def degrees_to_radians(angle):
    return math.radians(angle)


def radians_to_degrees(angle):
    return math.degrees(angle)


def normalize_angle(angle):
    """Normalize angle to 0–360 degrees."""
    return angle % 360


# ==========================
# TRIANGLE UTILITIES
# ==========================

def law_of_sines_side(side1, angle1, angle2):
    """
    Find an unknown side using the Law of Sines.
    Angles are in degrees.
    """
    return (
        side1 *
        math.sin(math.radians(angle2)) /
        math.sin(math.radians(angle1))
    )


def law_of_cosines_side(a, b, angle):
    """
    Find third side using Law of Cosines.
    """
    angle = math.radians(angle)
    return math.sqrt(
        a**2 +
        b**2 -
        2*a*b*math.cos(angle)
    )


def law_of_cosines_angle(a, b, c):
    """
    Find angle opposite side c.
    Returns degrees.
    """
    angle = math.acos(
        (a*a + b*b - c*c) / (2*a*b)
    )
    return math.degrees(angle)


# ==========================
# COORDINATE CONVERSIONS
# ==========================

def polar_to_cartesian(r, theta):
    theta = math.radians(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)


def cartesian_to_polar(x, y):
    r = math.sqrt(x*x + y*y)
    theta = math.degrees(math.atan2(y, x))
    return (r, theta)


# ==========================
# IDENTITIES
# ==========================

def pythagorean_identity(angle):
    """
    Returns sin²θ + cos²θ.
    """
    s = sin(angle)
    c = cos(angle)
    return s**2 + c**2


def double_angle_sin(angle):
    angle = math.radians(angle)
    return math.sin(2 * angle)


def double_angle_cos(angle):
    angle = math.radians(angle)
    return math.cos(2 * angle)


def half_angle_sin(angle):
    angle = math.radians(angle)
    return math.sin(angle / 2)


def half_angle_cos(angle):
    angle = math.radians(angle)
    return math.cos(angle / 2)


# ==========================
# MISCELLANEOUS
# ==========================

def angle_between_points(x1, y1, x2, y2):
    """
    Returns the angle (degrees) from point 1 to point 2.
    """
    return math.degrees(
        math.atan2(y2 - y1, x2 - x1)
    )


def bearing(x1, y1, x2, y2):
    """
    Compass bearing (0–360°).
    """
    return normalize_angle(
        angle_between_points(x1, y1, x2, y2)
    )