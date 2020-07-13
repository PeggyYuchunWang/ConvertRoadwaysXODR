class Road_Predecessor_Successor:
    """
        Represents the linkage between a road and its predecessor or its successor.

        Parameters
        ----------
        id : int
            ID of the linked element.
        type : str
            Type of the linked element. Either "road" or "junction."
        contact_point : str
            Contact point of the link on the linked element. Either "start" or "end."
        element_s : int
            Alternative to contact_point for virtual junctions. Signifies that the 
            connection occurs within the predecessor. Only can be used for element type "road."
        element_dir : int  
            For when element_s is in use. Indicates the direction on the predecessor from 
            which the road is entered.
    """
    def __init__(self, id = 0, type = "", contact_point = "", element_s = 0, element_dir = 0):
        self.id = int(id)
        self.type = str(type) 
        self.contact_point = str(contact_point) 
        self.element_s = int(element_s) 
        self.element_dir = int(element_dir) 
