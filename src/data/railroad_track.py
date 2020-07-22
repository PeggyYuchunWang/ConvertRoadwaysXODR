class Railroad_Track:
    """
    Represents the courses for rail bound traffic. Can either
    be a main track or a side track.

    Found within a Railroad element. 

    Parameters
    ----------   
    id : str
        Unique ID of the switch.
    s : float
        s-coordinate of the switch. For a Main Track, it is the 
        point where the Main and Side Track meet. For a Side Track,
        it is the s-coordinate of the switch on teh Side Track.
    dir : str
        For a Main Track, it is the direction relative to the 
        s-direction on the main track for entering the side track 
        via the switch. For a Side Track, it is the direction 
        relative to the s-direction on the side track for after
        entering it via the switch.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above. 
    
    """
    def __init__(self, id = "", s = 0, dir = "") -> None: 
        self.attrib = {
            "id" : str(id),
            "s" : float(s),
            "dir" : str(dir)
        }       
        

