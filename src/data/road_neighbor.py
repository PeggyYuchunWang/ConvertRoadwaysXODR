class Road_Neighbor:
    """
    Provides detailed information about the neighbor of a road.
    Neighbor must be of type Road.

    Found within a Road element.

    Parameters
    ----------
    side : str
        The side on which the neighbor is configured. Either "left"
        or "right."
    element_id : str
        ID of the linked element.
    element_dir: str 
        Direction of hte neighbor relative to road's own direction.
        Either "same" or "opposite."
    
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, side = "", element_id = "", element_dir = "") -> None:
        self.attrib = {
            "side" : str(side),
            "element_id" : str(element_id),
            "element_dir" : str(element_dir) 
        }
