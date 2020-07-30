class Road_Mark:
    """
    Detailed information about the lane markings.
    Defines the style of the line at the lane's outer border.
    For left lanes, this is the left border, for right lanes the right one.
    The style of the center lane that separates left and right lanes is
    determined by the Road_Mark element for the center lane.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        Lane_Section element.
    type : str
        Type of the road.
    weight : str
        Weight of the road mark.
    color : str
        Color of the road mark.
    material : str
        Material of the road mark.
    width : int
        Width of the road mark.
    lane_change : str
        Allows a lane change in the indicated direction, taking into account
        that lanes are numbered in ascending order from right to left. If the
        attribute is missing, “both” is used as default.
    height : int
        Height of the road mark.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    sway : Road_Mark_Sway
        Object to describe lane markings that are not straight.
    type : Road_Mark_Type
        Object to provide detailed information about road marking types and
        lines.
    explicit : Road_Mark_Explicit
        Object to provide detailed information about irregular road markings
        that cannot be described by repetitive line patterns.
    """
    def __init__(
        self,
        s_offset=0,
        type="",
        weight="",
        color="",
        material="",
        width=0,
        lane_change="both",
        height=0
    ) -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "type": str(type),
            "weight": str(weight),
            "color": str(color),
            "material": str(material),
            "width": float(width),
            "lane_change": str(lane_change),
            "height": float(height)
        }
        self.sway = None
        self.type = None
        self.explicit = None
