class Signal_Position_Road:
    """
    Describes the reference point of the physical position in
    road coordinates in cases where it deviates from 
    the logical position.
    
    Found within a Signal element.
    
    Parameters
    ----------   
    road_id : str   
        Unique ID of the referenced road.
    s : float
        Position (s-coordinate).
    t : float
        Position (t-coordinate).
    z_offset : float
        z-offset from road level to bottom edge of the signal.
    h_offset : float
        Heading offset fo the signal (relative to @orientation).
    pitch : float
        Pitch angle of the signal after applying h_offset, relative 
        to the inertial system.
    roll : float
        Roll angle of the signal after applying h_offset and pitch, relative to
        the inertial system.
 
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  
    
    """
    def __init__(self, road_id = "", s = 0, t = 0, z_offset = 0, h_offset = 0, pitch = 0, roll = 0) -> None:        
        self.attrib = {
            "road_id" : str(road_id),
            "s" : float(s),
            "t" : float(t),
            "z_offset" : float(z_offset),
            "h_offset" : float(h_offset),
            "pitch" : float(pitch),
            "roll" : float(roll)
        }

