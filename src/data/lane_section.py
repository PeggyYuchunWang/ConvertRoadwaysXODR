"""
    Lanes may be split into mulitple lane sections. Each Lane_Section
    contains a fixed number of lanes. If the number of lanes change,
    a new Lane_Section is required.
"""
import Lane
import Lane_Width

class Lane_Section:
    
    def __init__(self, s = 0, singleSide = False, center_lane = None):
        self.s = float(s)
        self.singleSide = bool(singleSide)
        self.center_lane = center_lane #Lane.py type with id=0
        self.left_lanes = []
        self.right_lanes = []