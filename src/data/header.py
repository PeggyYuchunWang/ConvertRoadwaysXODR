from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset

class Header():
    """
        First element within any OpenDRIVE file.

        Parameters
        ----------
        revMajor : int
            Major revision number of OpenDRIVE format
        revMinor : int
            Minor revision number of OpenDRIVE format (6 for OpenDRIVE 1.6)
        name : str
            Database name
        version : str
            Version of the network
        date : str
            Time/date of database creation
        north : float
            Maximum inertial y value
        south : float
            Minimum inertial y value
        east : float
            Maximum inertial x value
        west : float
            Minimum inertial x value        
        vendor : str
            Vendor name

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above
        geoReference : Geo_Reference
            Information about the geographic reference for an OpenDRIVE dataset.
        offset : Offset
            An offset of the whole dataset may be applied to avoid large coordinates and
            enable inertial relocation and re-orientation of datasets.
    """

    def __init__(self, revMajor = 0, revMinor = 0, name = "", version = "", 
                date = "", north = 0, south = 0, east = 0, west = 0) -> None:        
        self.attrib = {
            "revMajor" : int(revMajor),
            "revMinor" : int(revMinor),
            "name" : str(name),
            "version" : str(version),
            "date" : str(date),
            "north" : float(north),
            "south" : float(south),
            "east" : float(east),
            "west" : float(west),
            "vendor" : str("")
        }
        self.geoReference = None
        self.offset = None

    
