"""
    Shape of lateral profile is calculated:
    h(ds) = a + b*dt + c*dt^2 + d*dt^3
    where h is the height above the reference plane at a given position 
    and dt is distance perpendicular to the reference line between the start of a shape element
    and the given position.
    Shapes must be defined in combination with superelevation and road elevation
    There should be no lane offset when using shapes.
"""
class Lateral_Profile_Shape(abcd_base):
    def __init__(self, s = 0, t = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.s = float(s)
        self.t = float(t)