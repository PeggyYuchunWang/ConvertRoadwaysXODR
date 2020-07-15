from src.data.road_predecessor_successor import Road_Predecessor_Successor
from src.data.road_type import Road_Type

class Road:
    """
        Defines the basic characteristics of an individual road.

        Parameters
        ----------
        name : str
            Name of road. Can choose a name freely.
        length : int
            Total length of the reference line in the xy-plane.
        id : int
            Unique ID given to the road, stored within the database.
        junction : int
            Unique ID of the junction to which the road belongs 
        rule : str
            Basic rule for using the road. Right Hand Traffic default.
        
        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
        type : Road_Type
            Object used to define the main purpose of a road.
        predecessor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road 
            and the road that comes before it
        successor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road
            and the road that comes after it
    """
    def __init__(self, name = "", length = 0.0, id = 0, junction = 0, rule = "RHT") -> None:
        self.attrib = {
            "name" : str(""),
            "length" : float(length),
            "id" : int(id),
            "junction" : int(junction),
            "rule" : str(rule) 
        } 
        self.type = None
        self.predecessor = None
        self.successor = None
