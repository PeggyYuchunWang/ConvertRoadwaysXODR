import src.data.abcd_base as abcd_base

class Road_Mark_Sway(abcd_base.ABCD_base):
    """
    Describes lane markings that are not straight, but have sideway curves. 
    Relocates the lateral reference posiiton for a Road_Mark_Explicit element.
    
    Found within a Road_Mark element.

    Parameters
    ----------
    ds : float
        Start position (s-coordinate) relative to the
        s_offset in the given Road_Mark element.
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
    def __init__(self, ds = 0, a = 0, b = 0, c = 0, d = 0) -> None:
        super().__init__(a, b, c, d)
        self.attrib["ds"] = float(ds)