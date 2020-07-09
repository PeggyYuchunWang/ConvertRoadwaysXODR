import Geometry

class Spiral(Geometry):
    def __init__(self, curvStart = 0, curvEnd = 0):
        if curvStart == curvEnd:
            #curvStart and curvEnd cannot be the same
            print("invalid spiral instantiation")
            return
        self.curvStart = float(curvStart)
        self.curvEnd = float(curvEnd)
        