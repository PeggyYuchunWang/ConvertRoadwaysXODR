class Lanes:
    """
        All roads contain Lanes. The center lane has no width and acts as
        the reference line for the road with a lane number of zero.
        Lane numbering starts with 1 next to the center lane, descending in
        negative t-direction and ascending in the positive t-direction.

        Found within a Road element.
        
        Attributes
        ----------
        lane_offsets : list
            List of Lane_Offset elements to describe the shift of the 
            center lane away from the road reference line.
        lane_sections : list
            List of Lane_Section elements that each contain a fixed 
            number of lanes.

    """
    def __init__(self) -> None:
        self.lane_offsets = []
        self.lane_sections = []