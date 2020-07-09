"""
    Lane_Height is used to implement small-scale elevation, such as
    raising a pedestrian walkway.
"""

class Lane_Height:
    def __init__(self, sOffset = 0, inner = 0, outer = 0):
        self.sOffset = float(sOffset)
        self.inner = float(inner)
        self.outer = float(outer)