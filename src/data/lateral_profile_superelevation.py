"""
    Superelevation is calculation by:
    s(ds) = a + b*ds + c*ds^2 + d*ds^3
    where ds is the dsitance along the reference line between the start
    of a superelevation element and the given position.
"""

class Lateral_Profile_Superelevation(abcd_base):
    def __init__(self, s = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.s = float(s)