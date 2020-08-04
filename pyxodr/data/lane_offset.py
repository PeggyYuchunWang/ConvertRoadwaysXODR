import pyxodr.data.abcd_base as abcd_base


class LaneOffset(abcd_base.ABCDBase):
    """
    Describes the shift of the center lane away from the
    road reference line.

    Found within a Lanes element.

    Parameters
    ----------
    s : float
        Start position (s-coordinate).
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
    def __init__(self, s=0, a=0, b=0, c=0, d=0) -> None:
        super().__init__(a, b, c, d)
        self.attrib["s"] = float(s)
