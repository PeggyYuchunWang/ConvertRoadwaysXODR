class Lateral_Profile(Lateral_Profile_Superelevation, Lateral_Profile_Shape):
    def __init__(self, super_elevation = None, shape = None):
        self.super_elevation = super_elevation
        self.shape = shape