class LaneAccess:
    """
    Defines access restrictions for certain types of road users for a lane.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        LaneSection element.
    rule : str
        Specifies whether the participant given in the attribute restriction is
        allowed or denied access to the given lane.
    restriction : str
        Identifier of the participant to which the restriction applies.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s_offset=0, rule="allow", restriction="") -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "rule": str(rule),
            "restriction": str(restriction)
        }
