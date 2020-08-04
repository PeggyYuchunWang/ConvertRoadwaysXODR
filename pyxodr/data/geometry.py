class Geometry:
    """
    Allows for the generation of arbitrary road courses through the combination
    of different geometry elements (Line, Spiral, Arc, Poly3 and ParamPoly3).
    To avoid leaps in the curvature, it is recommended to use spirals to
    combine lines with arcs.

    Found within the plan_view of a Road element.

    Parameters
    ----------
    s : float
        Start posiiton (s-coordinate).
    x : float
        Start position (x inertial).
    y : float
        Start position (y-inertial).
    hdg : float
        Start orientation (inertial heading).
    length : float
        Length of the element's reference line.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    type : Spiral, Arc, Poly3, or ParamPoly3
        Object that specifies more information about the actual geometry
        of the Geometry element. If type = None, then the geometry specifies
        a line.
    """
    def __init__(self, s=0, x=0, y=0, hdg=0, length=0) -> None:
        self.attrib = {
            "s": float(s),
            "x": float(x),
            "y": float(y),
            "hdg": float(hdg),
            "length": float(length)
        }
        self.type = None
