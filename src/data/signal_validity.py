class Signal_Validity:
    """
    Allows for default validity of a signal to be replaced with 
    explicit validity information.

    Found within a Signal element.
    
    Parameters
    ----------   
    from_lane : str
        Minimum ID of the lanes for which the signal is valid.
    to_lane : str
        Maximum ID of the lanes for which the signal is valid.
 
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  
    
    """
    def __init__(self, from_lane = "", to_lane = "") -> None:        
        self.attrib = {
            "from_lane" : str(from_lane),
            "to_lane" : str(to_lane)
        }

