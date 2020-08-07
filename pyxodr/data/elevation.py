import pyxodr.data.abcd_base as abcd_base


class Elevation(abcd_base.ABCDBase):
    """
    Describes the elevation of a road along its reference line. 
    Road elevation is defined per road cross section, specified in meters.
    Default elevation is zero.

    Found within the elevation_profile of a Road element.

    Parameters
    ----------
    s : int
        Start position (s-coordinate).
    a : int
        Generic parameter a.
    b : int
        Generic parameter b.
    c : int
        Generic parameter c.
    d : int
        Generic parameter d.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """

    def __init__(self, s=0, a=0, b=0, c=0, d=0) -> None:
        super().__init__(a, b, c, d)
        self.attrib["s"] = float(s)
