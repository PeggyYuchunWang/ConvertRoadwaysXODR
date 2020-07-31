class Junction_Priority:
    """
    Provides information about priority of a connecting road over another
    connecting road.

    Found within a Junction element.

    Parameters
    ----------
    high : str
        ID of the prioritized connecting road.
    low : int
        ID of the connecting road with lower priority.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, high="", low="") -> None:
        self.attrib = {
            "high": str(high),
            "low": str(low),
        }
