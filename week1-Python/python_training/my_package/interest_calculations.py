""" Module for Interest calculations"""


def simple_interest(prin, ny, roi):
    """
    calculating SI
    :param prin: principal amount
    :param ny: no of years
    :param roi: rate of interest
    :return: SI,Total amount
    """
    si = prin * ny * roi/100
    amount = prin + si
    return si, amount


def compound_interest(prin, t, roi):
    """
    calculating compound interest
    :param prin: principal amount
    :param ny: no of years
    :param roi: rate of interest
    :return: Total amount
    """
    amount = prin* ((1+(roi/100))**(1*t))
    return amount
