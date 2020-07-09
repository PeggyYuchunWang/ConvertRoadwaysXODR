"""
    The width of a lane is defined once per Lane_Section.
    The center lane must have no width and must exist in its own Lane_Section 
"""

class Lane_Width(abcd_base):
    def __init__(self, sOffset = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.sOffset = float(sOffset)