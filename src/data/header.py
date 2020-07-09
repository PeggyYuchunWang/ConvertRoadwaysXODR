class Header:
    """
        First element within any OpenDRIVE file.
    """
    def __init__(self, revMajor = 0, revMinor = 0, name = "", version = "", 
                date = "", north = 0, south = 0, east = 0, west = 0):
        self.revMajor = int(revMajor)
        self.revMinor = int(revMinor)
        self.name = name
        self.version = version
        self.date = date
        self.north = float(north)
        self.south = float(south)
        self.east = float(east)
        self.west = float(west)
        self.vendor = ""

    
