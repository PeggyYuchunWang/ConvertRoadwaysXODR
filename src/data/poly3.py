"""
    The interpolation of a cubic polynom in x/y coordinate system is described by:
    y(x) = a + b*x + c*x^2 + d*x^3
    Using the local u/v-coordinate system increases flexibility in the curve definition:
    v(u) = a + b*u + c*u^2 + d*u^3
    The u/v-coordinate system should be aligned with the s/t-coordinate system
    at the segment's start position (Geometry.x, Geometry.y) and starting orientation
    (Geometry.hdg). 
"""
import Geometry
import abcd_base

class Poly3(Geometry, abcd_base):
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)