import pyxodr.data.abcd_base as abcd_base


class Lateral_Profile_Shape(abcd_base.ABCD_base):
    """
    Decribes the elevation of a road's cross section at a given point on the
    reference line. There may be several shape definitions at one s-coordinate
    that have different t-coordinates.

    Found within a the Lateral_Profile element.

    Parameters
    ----------
    s : float
        Start position (s-coordinate).
    t : float
        Start position (t-coordinate).
    a : float
        Generic parameter a.
    b : float
        Generic parameter b.
    c : float
        Generic parameter c.
    d : float
        Generic parameter d.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s=0, t=0, a=0, b=0, c=0, d=0) -> None:
        super().__init__(a, b, c, d)
        self.attrib["s"] = float(s)
        self.attrib["t"] = float(t)
