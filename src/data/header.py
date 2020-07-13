class Header:
    """
        First element within any OpenDRIVE file.
    """
    def __init__(self, revMajor = 0, revMinor = 0, name = "", version = "", 
                date = "", north = 0, south = 0, east = 0, west = 0):        
        self.attrib = {
            "revMajor" : int(revMajor),
            "revMinor" : int(revMinor),
            "name" : name,
            "version" : version,
            "date" : date,
            "north" : float(north),
            "south" : float(south),
            "east" : float(east),
            "west" : float(west),
            "vendor" : ""
        }
        self.geoReference = None
        self.offset = None

    
