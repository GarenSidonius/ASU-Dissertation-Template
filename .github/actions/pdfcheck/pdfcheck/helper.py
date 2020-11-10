""".. py:module:: pdfcheck.helper

Miscellenous helper functions"""


def points_2_inches(points) -> float:
    """
    Convert points to inches
    """
    return points / 72


def inches_2_points(inches) -> float:
    """
    Convert inches to points
    """
    return inches * 72
