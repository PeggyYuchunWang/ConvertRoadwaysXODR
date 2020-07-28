class Lane_Speed:
    """
    Defines the maximum allowed speed on a give lane. Lane_Speed overrides any
    Road_Speed limits.

    If there are multiple lane speed limit elements per lane section, the
    elements must be defined in ascending order.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        Lane_Section element.
    max : int
        Maximum speed allowed.
    unit : str
        Units for the speed.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s_offset=0, max=0, unit="") -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "max": float(max),
            "unit": str(unit)
        }
