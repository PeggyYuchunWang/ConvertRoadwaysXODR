from src.data.road_predecessor_successor import Road_Predecessor_Successor

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
        predecessor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road 
            and the road that comes before it
        successor : Road_Predecessor_Successor
            Object used to represent the linkage between the current road
            and the road that comes after it
    """
    def __init__(self, name = "", length = 0, id = 0, junction = 0, rule = "RHT"):
        self.name = str("")
        self.length = float(length)
        self.id = int(id)
        self.junction = int(junction)
        self.rule = str(rule) #if no rule provided, RHT is assumed
        self.predecessor = None
        self.successor = None
