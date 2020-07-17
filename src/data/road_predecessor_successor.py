class Road_Predecessor_Successor:
    """
    Represents the linkage between a road and its predecessor or its successor.

    Found within a Road element.

    Parameters
    ----------
    element_id : str
        ID of the linked element.
    element_type : str
        Type of the linked element. Either "road" or "junction."
    contact_point : str
        Contact point of the link on the linked element. Either "start" or "end."
    element_s : float
        Alternative to contact_point for virtual junctions. Signifies that the 
        connection occurs within the predecessor. Only can be used for element type "Road."
    element_dir: str 
        For when element_s is in use. Indicates the direction on the predecessor from 
        which the road is entered.
    
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, element_id = "", element_type = "", contact_point = "", element_s = 0, element_dir = "") -> None:
        self.attrib = {
            "element_id" : str(element_id),
            "element_type" : str(element_type), 
            "contact_point" : str(contact_point), 
            "element_s" : float(element_s), 
            "element_dir" : str(element_dir) 
        }
