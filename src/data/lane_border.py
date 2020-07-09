"""
    Another way to describe the width of lanes. Lane_Border describes the outer limits of a lane,
    independent of the parameters of their inner borders.

    Lane_Width and Lane_Border are mutually exclusive.
"""

class Lane_Border(abcd_base):
    def __init__(self, sOffset = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.sOffset = float(sOffset)