class Object_Marking:
    """
    Specifies a marking that is either attached to one side of 
    an object's bounding box or referencing outline points.

    Found within an Object element.
    
    Parameters
    ----------   
    side : str
        Side of the bounding box described in Object.
    weight : str
        Optical weight of the marking. Either "standard" or "bold."
    width : float
        Width of the marking.
    color : str
        Color of the marking.
    z_offset : float
        Height of marking above the road.
    space_length : float
        Length of the gap between the visible parts.
    line_length : float
        Length of the visible parts.
    start_offset : float
        Lateral offset in u-direction from start of bounding box
        side where the first marking starts.
    stop_offset : float
        Lateral offset in u-direction from end of bounding box 
        side where the marking ends.
    
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  
    corner_references : list
        List of maximum two IDs that define the marking as a straight
        line from one outline point to another. 

    """
    def __init__(self, side = "", weight = "standard", width = 0, color = "", z_offset = 0,
                 space_length = 0, line_length = 0, start_offset = 0, stop_offset = 0) -> None:        
        self.attrib = {
            "side" : str(side),
            "weight" : str(weight),
            "wdith" : float(width),
            "color" : str(color),
            "z_offset" : float(z_offset),
            "space_length" : float(space_length),
            "line_length" : float(line_length),
            "start_offset" : float(start_offset),
            "stop_offset" : float(stop_offset)
        }
        self.corner_references = []
