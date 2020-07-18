class Junction:
    """
    Contains information about all possible connections between 
    roads meetings at a physical junction.

    Parameters
    ----------
    name : str
        Name of road. Can choose a name freely.
    id : str
        Unique ID given to the road, stored within the database.
    type : str
        Type of the junction. Either "default" or "virtual."
       
    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.    
    connections : list
        List of Junction_Connection elements to provide 
        information about a single conenction within a junction.  
    controller : list
        List of Junction_Control elements that are used 
        for the management of a junction.  
    """
    def __init__(self, name = "", id = "", type = "") -> None:
        self.attrib = {
            "name" : str(name),
            "id" : str(id),            
            "type" : str(type)
        }      
        self.connections = []
        self.controllers = []
 
        #the following attributes are included in OpenCRG
        #will we be including these?
        # self.surface = None
        # self.mode = None
        # self.purpose = None

