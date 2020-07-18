class Junction_Lane_Link:
    """
    Provides information about the lanes that are linked
    between an incoming road and a connecting road.

    Found within a Junction_Connection element.

    Parameters
    ----------
    from_id : int
        ID of the incoming lane.
    to_id : int
        ID of the connection lane.
      
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.        
    """
    def __init__(self, from_id = 0, to_id = 0) -> None:
        self.attrib = {
            "from_id" : int(from_id),            
            "to_id" : int(to_id),
        }      

