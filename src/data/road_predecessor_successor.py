class Road_Predecessor_Successor:
    """
        Represents the linkage between a road and its predecessor or its successor.

        Parameters
        ----------
        id : int
            ID of the linked element.
        type : str
            Type of the linked element. Either "road" or "junction."
        contactPoint : str
            Contact point of the link on the linked element. Either "start" or "end."
        elementS : int
            Alternative to contact_point for virtual junctions. Signifies that the 
            connection occurs within the predecessor. Only can be used for element type "road."
        elementDir: int  
            For when element_s is in use. Indicates the direction on the predecessor from 
            which the road is entered.
        
        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
    """
    def __init__(self, id = 0, type = "", contactPoint = "", elementS = 0, elementDir = 0) -> None:
        self.attrib = {
            "id" : int(id),
            "type" : str(type), 
            "contactPoint" : str(contactPoint), 
            "elementS" : int(elementS), 
            "elementDir" : int(elementDir) 
        }
