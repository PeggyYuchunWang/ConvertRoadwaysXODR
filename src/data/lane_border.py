import src.data.abcd_base as abcd_base


class Lane_Border(abcd_base.ABCD_base):
    """
    Another method to describe the width of lanes.
    Describes the outer limits of a lane, independent of the parameters of
    their inner borders.

    Lane_Width and Lane_Border are mutually exclusive.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        Lane_Section element.
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
