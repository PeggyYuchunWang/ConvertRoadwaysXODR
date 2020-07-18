class Junction_Group:
    """
    Provides a groupiong for two or more junctions to indicate
    that these junctions belong to the same roundabout.

    Parameters
    ----------
    name : str
        Name of the junction group. Can choose a name freely.
    id : str
        Unique ID given to the group, stored within the database.
    type : str
        Type of the junction group. Either "roundabout" or "unknown."
       
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.    
    junction_references : list
        List of string IDs of the junctions in the group. 

    """
    def __init__(self, name = "", id = "", type = "") -> None:
        self.attrib = {
            "name" : str(name),
            "id" : str(id),            
            "type" : str(type)
        }      
        self.junction_references = []

