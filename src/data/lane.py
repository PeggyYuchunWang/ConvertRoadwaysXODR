class Lane:
    """
        Defines the main purpose of a lane.

        Left Lanes must have negative id values, right Lanes 
        must have positive id values and center Lanes have an id value of 0.

        If linkage between lanes is ambiguous, junctions must be used. Otherwise, specify
        the predecessor ID / successor ID for the Lane.

        Found within a Lanes element.

        Parameters
        ----------
        id : int
            ID of the lane
        type : str
            Defines the main purpose of a lane and its corresponding traffic rules.
        level : bool
            Specifies either to keep lane on level or apply superelevation. 
            Default is false, which corresponds to applying superelevation to the lane.

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
        predecessor_id : int
            ID of preceeding lane.
        successor_id : int
            ID of succeeding lane.
        width : Lane_Width
            Object to describe the width of a lane defined along the
            t-coordinate.
        border : Lane_Border
            
        lane_material : Lane_Material
            ??????
 
    """
    def __init__(self, id = 0, type = "", level = False) -> None:
        self.attrib = {
            "id" : int(id),
            "type" : None,
            "level" : False
        }      
        self.predecessor_id = None 
        self.successor_id = None 
        self.width = None
        self.border = None
        self.lane_material = None
        self.road_mark = None



