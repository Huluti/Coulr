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

def rgb_floats_to_int(rgb_floats):
    """Convert RGB floats color to RGB (int) color.
    :param rgb_floats: RGB floats color from Gtk.Color
    :type rgb_floats: tuple
    :return: RGB color
    :rtype: tuple

    """

    return tuple(int(rgb_floats[i]*255) for i in range(3))