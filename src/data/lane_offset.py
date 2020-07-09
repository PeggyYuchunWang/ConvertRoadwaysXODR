"""
    Used to shift the center lane away from the road reference line.
    Lane_Offset should not be used together with Lateral_Profile_Shape.
    
"""
from abcd_base import abcd_base

class Lane_Offset(abcd_base):
    def __init__(self, s = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.s = float(s)
        