class Lane_Section:
    """
    Contains a fixed number of lanes. A new Lane_Section is
    required when the number of lanes changes. 

    Found within a Lanes element.

    Parameters
    ----------
    s : float
        Start position (s-coordinate).
    single_side : bool
        Specifies if the lane section is valid for only one
        side (left, center or right), depending on the child elements.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    center_lane : Lane
        The center Lane element with an ID of zero.
    left_lanes : list
        List of lanes to the left of the center_lane. Every left Lane must
        have a negative ID value.
    right_lanes : list
        List of lanes to the right of the center_lane. Every right Lane must
        have a positive ID value.
    """
    def __init__(self, s = 0) -> None:
        self.attrib = {
            "s" : float(s),
            "single_side" : False
        }      
        self.center_lane = None
        self.left_lanes = []
        self.right_lanes = []
        