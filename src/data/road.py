from src.data.road_predecessor_successor import Road_Predecessor_Successor
from src.data.road_type import Road_Type

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
        type : Road_Type
            Object used to define the main purpose of a road.
        predecessor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road 
            and the road that comes before it.
        successor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road
            and the road that comes after it.
        plan_view : list
            List of geometrys describing the road's reference line.
        elevation_profile : Elevation
            Object used to describe the elevation of a road along its reference line. 
        lateral_profile : dict
            Dictionary to contain Lateral_Profile_Superelevation and a list of 
            Lateral_Profile_Shape elements if needed. Defines the characteristics of the 
            road surface's banking along the reference line.
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
        self.type = None
        self.predecessor = None
        self.successor = None
        self.plan_view = []
        self.elevation_profile = None
        self.lateral_profile = {
            "super_elevation" : None,
            "shapes" : []
        }
        self.lanes = None
