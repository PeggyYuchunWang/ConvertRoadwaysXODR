""" 
    Parent class for Spiral, Arc, Poly3 and ParamPoly3
    
    Allows for the generation of arbitrary road courses through the combination
    of different geometry elements (Spiral.py, Arc.py). To avoid leaps in the curvature,
    it is recommended to use spirals to combine lines with arcs. 
"""

class Geometry:
    def __init__(self, s = 0, x = 0, y = 0, hdg = 0, length = 0):
        self.s = float(s)
        self.x = float(x)
        self.y = float(y)
        self.hdg = float(hdg)
        self.length = float(length)
        #self.type = None ***Unsure if we need this***