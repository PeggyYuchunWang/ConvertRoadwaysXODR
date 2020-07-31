class Lateral_Profile:
    """
    Using superelevation and shape definition, specifies the elevation
    orthogonally to the reference line, that is in t-direction.

    Found within a Road element.

    Parameters
    ----------
    super_elevation : Lateral_Profile_Superelevation
        Object to define a road section's roll angle around the s-axis.
    shapes : list
        List of Lateral_Profile_Shape elements.
    """
    def __init__(self, super_elevation=None, shapes=[]) -> None:
        self.super_elevation = super_elevation
        self.shapes = shapes
