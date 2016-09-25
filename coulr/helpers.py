#!/usr/bin/env python

def rgb_to_hex(rgb):
    """Convert RGB color to hex color."
    :param rgb: RGB color
    :type rgb: tuple
    :return: Hex color
    :rtype: str

    """

    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

def hex_to_rgb(hexa):
    """Convert hex color to RGB color.
    :param hexa: Hex color
    :type hexa: str
    :return: RGB color
    :rtype: tuple

    """
    
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))
