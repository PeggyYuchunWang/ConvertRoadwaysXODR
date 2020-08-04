class LaneHeight:
    """
    Implements small-scale elevation, such as raising a pedestrian walkway.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        LaneSection element.
    inner : float
        Inner offset from the road level.
    outer : float
        Outer offset from the road level.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s_offset=0, inner=0, outer=0) -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "inner": float(inner),
            "outer": float(outer)
        }
