class Header:
    """
        First element within any OpenDRIVE file.

        Parameters
        ----------
        rev_major : int
            Major revision number of OpenDRIVE format.
        rev_minor : int
            Minor revision number of OpenDRIVE format (6 for OpenDRIVE 1.6).
        name : str
            Database name.
        version : str
            Version of the network.
        date : str
            Time/date of database creation.
        north : float
            Maximum inertial y value.
        south : float
            Minimum inertial y value.
        east : float
            Maximum inertial x value.
        west : float
            Minimum inertial x value.     
        vendor : str
            Vendor name.

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
        geo_reference : Geo_Reference
            Object to define the geographic reference for an OpenDRIVE dataset.
        offset : Offset
            Object to define an offset of the whole dataset that may be 
            applied to avoid large coordinates and enable inertial 
            relocation and re-orientation of datasets.
    """

    def __init__(self, rev_major = 0, rev_minor = 0, name = "", version = "", 
                date = "", north = 0, south = 0, east = 0, west = 0) -> None:        
        self.attrib = {
            "rev_major" : int(rev_major),
            "rev_minor" : int(rev_minor),
            "name" : str(name),
            "version" : str(version),
            "date" : str(date),
            "north" : float(north),
            "south" : float(south),
            "east" : float(east),
            "west" : float(west),
            "vendor" : str("")
        }
        self.geo_reference = None
        self.offset = None

    
