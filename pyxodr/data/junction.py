class Junction:
    """
    Contains information about all possible connections between roads meetings
    at a physical junction.

    Parameters
    ----------
    id : str
        Unique ID given to the road, stored within the database.
    name : str
        Name of road. Can choose a name freely.
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
    priorities : list
        List of Junction_Priority elements that are used to determine
        the priority of connecting roads if priorities cannot
        be derived from signs or signals in a junction.
    """
    def __init__(self,  id="", name="", type="") -> None:
        self.attrib = {
            "id": str(id),
            "name": str(name),
            "type": str(type)
        }
        self.connections = []
        self.controllers = []
        self.priorities = []

        # the following attributes are included in OpenCRG
        # will we be including these?
        # self.surface = None
        # self.mode = None
        # self.purpose = None
