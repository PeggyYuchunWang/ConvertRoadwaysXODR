class Railroad:
    """
    Container for all rail-based transport systems.

    Found within a Road element.

    Attributes
    ----------
    switches : dict
        Dictionary of Railroad_Switch elements found along the specified road.
    """
    def __init__(self) -> None:
        self.switches = {}