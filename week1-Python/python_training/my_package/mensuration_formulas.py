""" Area, Circumference of SQ, RECT, CIRCLE"""
from math import pi


def area_of_square(side):
    """Area of square
    :param side: side of square
    :return:Area
    """
    return side * side

def area_of_circle(rad):
    """Area of circle
    :param side: side of circle
    :return:Area
    """
    return pi * rad * rad



def area_of_rect(len, brd):
    return len * brd

