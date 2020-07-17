class Lane_Rule:
    """
    Further description on lane properties which are 
    not covered by any of the other lane attributes defined within
    this framework.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the 
        preceding Lane_Section element.
    value : str
        Free text, with current recommended values being:
            "no stopping at any time"
            "disabled parking"
            "car pool"

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s_offset = 0, value = "") -> None:
        self.attrib = {
            "s_offset" : float(s_offset),
            "value" : str(value)
        }
        