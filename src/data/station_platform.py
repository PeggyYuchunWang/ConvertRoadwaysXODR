class Station_Platform:
    """
    Defines a platform for a station.

    Found within a Station element.

    Parameters
    ----------
    id : str
        Unique ID within the database.
    name : str
        Name of the platform. May be chosen freely.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.  
    segments : list
        List of Station_Segment elements that describe the track 
        segments for which a platform is valid.
    
    
    """
    def __init__(self,
                id = "",
                name = "") -> None:        
        self.attrib = {
            "id" : str(id),
            "name" : str(name)
        }
        self.segments = []


