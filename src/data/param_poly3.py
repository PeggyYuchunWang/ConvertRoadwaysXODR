class Param_Poly3:
    """
    Describes a part of a road's reference line as a parametric cubic curve.

    Found within a Geometry element.

    Parameters
    ----------
    p_range : str
        Range of parameter p. Either "arcLength" or "normalized."
    aU : float
        Polynom parameter for u.
    bU : float
        Polynom parameter for u.
    cU : float
        Polynom parameter for u.
    dU : float
        Polynom parameter for u.
    aV : float
        Polynom parameter for v.
    bV : float
        Polynom parameter for v.
    cV : float
        Polynom parameter for v.
    dV : float
        Polynom parameter for v.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(
        self,
        p_range="",
        aU=0,
        bU=0,
        cU=0,
        dU=0,
        aV=0,
        bV=0,
        cV=0,
        dV=0
    ) -> None:
        self.attrib = {
            "p_range": str(p_range),
            "aU": float(aU),
            "bU": float(bU),
            "cU": float(cU),
            "dU": float(dU),
            "aV": float(aV),
            "bV": float(bV),
            "cV": float(cV),
            "dV": float(dV)
        }
