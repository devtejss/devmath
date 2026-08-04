"""
devmath.geometry
Geometry functions for 2D and 3D shapes.
"""

import math


# ======================
# AREA
# ======================

def area_square(side):
    return side ** 2


def area_rectangle(length, width):
    return length * width


def area_triangle(base, height):
    return 0.5 * base * height


def area_circle(radius):
    return math.pi * radius ** 2


def area_parallelogram(base, height):
    return base * height


def area_trapezium(a, b, height):
    return 0.5 * (a + b) * height


def area_rhombus(d1, d2):
    return 0.5 * d1 * d2


def area_ellipse(a, b):
    return math.pi * a * b


def area_equilateral_triangle(side):
    return (math.sqrt(3) / 4) * side ** 2


def area_regular_polygon(n, side):
    return (n * side ** 2) / (4 * math.tan(math.pi / n))


# ======================
# PERIMETER
# ======================

def perimeter_square(side):
    return 4 * side


def perimeter_rectangle(length, width):
    return 2 * (length + width)


def perimeter_triangle(a, b, c):
    return a + b + c


def circumference(radius):
    return 2 * math.pi * radius


def perimeter_parallelogram(a, b):
    return 2 * (a + b)


def perimeter_rhombus(side):
    return 4 * side


# ======================
# VOLUME
# ======================

def volume_cube(side):
    return side ** 3


def volume_cuboid(length, width, height):
    return length * width * height


def volume_sphere(radius):
    return (4 / 3) * math.pi * radius ** 3


def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height


def volume_cone(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height


def volume_prism(base_area, height):
    return base_area * height


def volume_pyramid(base_area, height):
    return base_area * height / 3


# ======================
# SURFACE AREA
# ======================

def surface_area_cube(side):
    return 6 * side ** 2


def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)


def surface_area_sphere(radius):
    return 4 * math.pi * radius ** 2


def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)


def surface_area_cone(radius, slant_height):
    return math.pi * radius * (radius + slant_height)


# ======================
# DISTANCE
# ======================

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def midpoint_2d(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def midpoint_3d(x1, y1, z1, x2, y2, z2):
    return (
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        (z1 + z2) / 2
    )


# ======================
# ANGLES
# ======================

def degrees_to_radians(angle):
    return math.radians(angle)


def radians_to_degrees(angle):
    return math.degrees(angle)


# ======================
# PYTHAGORAS
# ======================

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def missing_side(hypotenuse, side):
    return math.sqrt(hypotenuse ** 2 - side ** 2)


# ======================
# CIRCLE
# ======================

def arc_length(radius, angle_degrees):
    return (angle_degrees / 360) * 2 * math.pi * radius


def sector_area(radius, angle_degrees):
    return (angle_degrees / 360) * math.pi * radius ** 2


def chord_length(radius, angle_degrees):
    angle = math.radians(angle_degrees)
    return 2 * radius * math.sin(angle / 2)


# ======================
# POLYGONS
# ======================

def interior_angle_regular_polygon(n):
    return ((n - 2) * 180) / n


def exterior_angle_regular_polygon(n):
    return 360 / n


def sum_interior_angles(n):
    return (n - 2) * 180


# ======================
# COORDINATE GEOMETRY
# ======================

def slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ZeroDivisionError("Slope is undefined.")
    return (y2 - y1) / (x2 - x1)


def line_length(x1, y1, x2, y2):
    return distance_2d(x1, y1, x2, y2)


def centroid_triangle(x1, y1, x2, y2, x3, y3):
    return (
        (x1 + x2 + x3) / 3,
        (y1 + y2 + y3) / 3
    )