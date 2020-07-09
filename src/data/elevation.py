"""
    Road elevation is calulated with the following polynomial thrid order function:
    elev(ds) = a + b*ds + c*ds^2 + d*ds^3
    ds = distance along reference line between the start of a new elevation element
    and the given position
"""

class Elevation(abcd_base):
    def __init__(self, s = 0, a = =, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.s = float(s)