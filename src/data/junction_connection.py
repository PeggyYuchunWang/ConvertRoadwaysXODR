class Junction_Connection:
    """
    Provides information about a signle connection within a junction.

    Found within a Junction element.

    Parameters
    ----------
    id : str
        Unique ID within the junction.
    type : str
        Type of the connection. Either "default" or "virtual."
    incoming_road : str
        ID of the incoming road.
    connecting_road : str
        ID of the connecting road.
    contact_point : str
        Contact point on the connecting road. Either "start" or "end."
       
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.    
    predecessor : Junction_Predecessor_Successor
        Object used to represent the linkage between the current junction
        and the road that comes before it.
    successor : Junction_Predecessor_Successor
        Object used to represent the linkage between the current junction
        and the road that comes after it.
    lane_links : list
        List of Junction_Lane_Link elements to provide information about 
        the lanes that are linked between an incoming road and a 
        connecting road.   
    """
    def __init__(self, id = "", type = "", incoming_road = "", connecting_road = "", contact_point = "") -> None:
        self.attrib = {
            "id" : str(id),            
            "type" : str(type),
            "incoming_road" : str(incoming_road),
            "connecting_road" : str(connecting_road),
            "contact_point" : str(contact_point)
        }
        self.predecessor = None
        self.successor = None  
        self.lane_links = []  

