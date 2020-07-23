class Station_Platform_Segment:
    """
    Defines which track segments a station platform is valid.

    Found within a Station_Platform element.

    Parameters
    ----------
    road_id : str
        Unique ID of the road which accompanies the platform.
    s_start : float
        Minimum s-value on road where platform is adjacent to it.
    s_end : float
        Maximum s-value on road where platform is adjacent to it.
    side : str
        Side of the track where platform is situated when going from 
        @s_start to @s_end.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.   
    """
    def __init__(self,
                road_id = "",
                s_start = 0,
                s_end = 0,
                side = "") -> None:        
        self.attrib = {
            "road_id" : str(road_id),
            "s_start" : float(s_start),
            "s_end" : float(s_end),
            "side" : str(side)
        }


