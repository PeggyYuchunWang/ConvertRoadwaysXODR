class Object_Reference:
    """
    Allows an object to be linked with one or more roads,
    signals or other objects. 
    
    Found within an Objects element.
    
    Parameters
    ----------   
    s : float
        Position (s-coordinate).
    t : float
        Position (t-coordinate).
    id : str
        Unique ID of the referred object within the database
    z_offset : float
        z-offset relative to the elevation of the reference line.
    valid_length : float
        Length of the validity of the object along s-axis.
    orientation : str
        Determines the validity in the s-direction. Either "+"=valid in positive
        s-direction, "-"=valid in negative s-direction or "none"=valid in 
        both directions.
    
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  

    """
    def __init__(self, s = 0, t = 0, id = "", z_offset = 0, valid_length = 0, orientation = "") -> None:        
        self.attrib = {
            "s" : float(s),
            "t" : float(t),
            "id" : str(id),
            "z_offset" : float(z_offset),
            "valid_length" : float(valid_length),
            "orientation" : str(orientation)                  
        }
