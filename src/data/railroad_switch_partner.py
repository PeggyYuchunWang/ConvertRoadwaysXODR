class Railroad_Switch_Partner:
    """
    Defines the switch that leads out of a side track 
    after is has been entered.

    Found within a Railroad element. 

    Parameters
    ----------   
    name : str
        Unique name of the partner switch.
    id : str
        Unique ID of the partner switch.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above. 
    
    """
    def __init__(self, name = "", id = "") -> None: 
        self.attrib = {
            "name" : str(name),
            "id" : str(id)
        }       
        

