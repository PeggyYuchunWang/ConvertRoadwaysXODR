class Road:
    """
    Defines the basic characteristics of an individual road.

    Parameters
    ----------
    id : int
        Unique ID given to the road, stored within the database.
    length : int
        Total length of the reference line in the xy-plane.
    junction : int
        Unique ID of the junction to which the road belongs.
    rule : str
        Basic rule for using the road. Right Hand Traffic default.
    name : str
        Name of road. Can choose a name freely.
    
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.        
    predecessor : Road_Predecessor_Successor
        Object used to represent the linkage between the current road 
        and the road that comes before it.
    successor : Road_Predecessor_Successor
        Object used to represent the linkage between the current road
        and the road that comes after it.
    type : Road_Type
        Object used to define the main purpose of a road.
    plan_view : list
        List of Geometry elements describing the road's reference line.
    elevation_profile : list
        List of Elevation elements describing the elevation of a road 
        along its reference line. 
    lateral_profile : Lateral_Profile
        Object to define the characteristics of the road surface's 
        banking along the reference line.
    lanes : Lanes
        Object used to represent all lane sections.
    """
    def __init__(self, id = "", length = 0,  junction = "-1", rule = "RHT", name = "") -> None:
        self.attrib = {
            "id" : str(id),            
            "length" : float(length),           
            "junction" : str(junction),
            "rule" : str(rule),
            "name" : str("") 
        }      
        self.predecessor = None
        self.successor = None
        self.type = None
        self.plan_view = []
        self.elevation_profile = []
        self.lateral_profile = None
        self.lanes = None
        #self.objects = None
