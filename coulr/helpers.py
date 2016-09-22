#!/usr/bin/env python

def rgb_to_hex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

def hex_to_rgb(hexa):
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2 ,4))
