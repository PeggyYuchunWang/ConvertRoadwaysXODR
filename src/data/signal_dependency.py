class Signal_Dependency:
    """
    Allows a signal to control one or more other signals.
    
    Found within a Signal element.
    
    Parameters
    ----------   
    id : str
        ID of the controlled signal
    type : str
        Type of the dependency. Free text, depending on application.
 
    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  
    
    """
    def __init__(self, id = "", type = "") -> None:        
        self.attrib = {
            "id" : str(id),
            "type" : str(type)
        }

