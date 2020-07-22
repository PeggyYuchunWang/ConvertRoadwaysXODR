class Object_Bridge:
    """
    Details about a bridge element. Valid for the complete corss section of a road.

    Found within an Objects element.
    
    Parameters
    ----------   
    s : float
        Position (s-coordinate).
    length : float
        Length of the tunnel (in s-direction).
    id : str
        Unique ID within database.
    type : str
        Type of the tunnel. For values, see UML Model.  
    name : str
        Name of the tunnel. May be chosen freely.
    
    
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  

    """
    def __init__(self, s = 0, length = 0, id = "" , type = "", name = "") -> None:        
        self.attrib = {
               "s" : float(s),
               "length" : float(length),
               "id" : str(id),
               "type" : str(type),
               "name" : str(name)
        }
