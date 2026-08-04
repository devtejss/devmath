"""
devmath.exceptions
Custom exceptions for DevMath.
"""

class DevMathError(Exception):
    """Base exception for DevMath."""
    pass


class MatrixError(DevMathError):
    """Raised for invalid matrix operations."""
    pass


class GeometryError(DevMathError):
    """Raised for geometry-related errors."""
    pass


class AlgebraError(DevMathError):
    """Raised for algebra-related errors."""
    pass


class StatisticsError(DevMathError):
    """Raised for statistics-related errors."""
    pass