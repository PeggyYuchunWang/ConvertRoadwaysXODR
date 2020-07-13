class Geo_Reference:
    """
        Information about the geographic reference for an OpenDRIVE dataset. 
        Defined by parameters describing the geodetic datum. 
        
        A geodetic datum is a coordinate reference system for a collection 
        of positions that are relative to an ellipsoid model of the earth.
        A geodetic datum is described by a projection string according to PROJ, 
        that is, a format for the exchange of data between two coordinate systems.
        
        Found within the Header element.

        Parameters
        ----------
        text : str
            proj-string that contains all parameters that define the 
            spatial reference system
    """
    def __init__(self, text = ""):
        self.text = text