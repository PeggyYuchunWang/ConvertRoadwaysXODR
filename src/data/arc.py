class Arc:
    """
    Describes part of the road's reference line as an Arc.

    Found within a Geometry element.

    Parameters
    ----------
    curvature : float
        Constant curvature throughout the Arc element.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, curvature = 0) -> None:
        self.attrib = {
            "curvature" : float(curvature)     
        }
        