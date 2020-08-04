import pyxodr.data.abcd_base as abcd_base


class LaneWidth(abcd_base.ABCDBase):
    """
    Specifies the width of a lane. Center lanes do not have a width.

    LaneWidth and LaneBorder are mutually exclusive.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        LaneSection element.
    a : float
        Polynom parameter a.
    b : float
        Polynom parameter b.
    c : float
        Polynom parameter c.
    d : float
        Polynom parameter d.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s_offset=0, a=0, b=0, c=0, d=0):
        super().__init__(a, b, c, d)
        self.attrib["s_offset"] = float(s_offset)