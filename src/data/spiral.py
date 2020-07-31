class Spiral():
    """
    Describes a part of the road's reference line as a Spiral.

    Found within a Geometry element.

    Parameters
    ----------
    curv_start : float
        Curvature at the start of the Spiral element.
    curv_end : float
        Curvature at the end of the Spiral element.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, curv_start=0, curv_end=0) -> None:
        self.attrib = {
            "curv_start": float(curv_start),
            "curv_end": float(curv_end)
        }
