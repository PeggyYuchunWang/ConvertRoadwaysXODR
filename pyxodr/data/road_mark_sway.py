import pyxodr.data.abcd_base as abcd_base


class RoadMarkSway(abcd_base.ABCDBase):
    """
    Describes lane markings that are not straight, but have sideway curves.
    Relocates the lateral reference position for a RoadMarkExplicit element.

    Found within a RoadMark element.

    Parameters
    ----------
    ds : float
        Start position (s-coordinate) relative to the
        s_offset in the given RoadMark element.
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
    def __init__(self, ds=0, a=0, b=0, c=0, d=0) -> None:
        super().__init__(a, b, c, d)
        self.attrib["ds"] = float(ds)
