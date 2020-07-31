class Lane:
    """
    Defines the main purpose of a lane.

    Left Lanes must have positive id values,
    right Lanes must have negative id values
    and center Lanes have an id value of 0.

    If linkage between lanes is ambiguous, junctions must be used.
    Otherwise, specify the predecessor ID / successor ID for the Lane.

    Found within a Lane_Section element.

    Parameters
    ----------
    id : int
        ID of the lane
    type : str
        Defines the main purpose of a lane and its corresponding traffic rules.
    level : bool
        Specifies either to keep lane on level or apply superelevation.
        Default is false, which corresponds to applying superelevation to the
        lane.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    predecessor_id : int
        ID of preceding lane.
    successor_id : int
        ID of succeeding lane.
    width : Lane_Width
        Object to describe the width of a lane defined along the
        t-coordinate.
    border : Lane_Border
        Object to describe the outer limits of a lane, independent
        of the parameters of their inner borders.
    road_mark : Road_Mark
        Object to provide detailed information about road marking
        types and lines.
    material : Lane_Material
        Object to describe the material of the lane.
    visibility : Lane_Visibility
        Object to describe the visibility in four directions relative
        to the lane's direction.
    speed : Lane_Speed
        Object to define the maximum allowed speed.
    access : Lane_Access
        Object to define access restrictions for certain types of
        road users.
    rule : Lane_Rule
        Object to provide further description on lane properties which are
        not covered by any of the other lane attributes defined within
        this framework.
    """
    def __init__(self, id=0, type="", level=False) -> None:
        self.attrib = {
            "id": int(id),
            "type": str(type),
            "level": bool(level)
        }
        self.predecessor_id = None
        self.successor_id = None
        self.width = None
        self.height = None
        self.border = None
        self.road_mark = None
        self.material = None
        self.visibility = None
        self.speed = None
        self.access = None
        self.rule = None
