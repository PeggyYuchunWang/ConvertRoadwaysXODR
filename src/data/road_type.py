class Road_Type():
    """
    Defines the main purpose of a road and the associated traffic rules.

    Valid for the entire cross section of a road, until a new road type element
    is provided or until the road ends. Country code and state identifier may 
    be added to specify national traffic rules. This will not
    be specified by OpenDRIVE. Only use ALPHA-r country codes.

    Found within a Road element.

    Parameters
    ----------
    s : float
        s-coordinate of start position.
    type : str
        Country code of the road (see ISO 3166-1 alpha-2 codes).
    country : str
        Country code of the road (see ISO 3166-1 alpha-2 codes).

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
"""
    def __init__(self, s = 0, type = "", country = ""):
        self.attrib = {
            "s" : float(s),
            "type" : str(type),
            "country" : str(country)
        }
        