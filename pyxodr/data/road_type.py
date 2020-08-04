class RoadType():
    """
    Defines the main purpose of a road and the associated traffic rules.

    Valid for the entire cross section of a road, until a new road type element
    is provided or until the road ends. Country code and state identifier may
    be added to specify national traffic rules. This will not be specified by
    OpenDRIVE. Only use ALPHA-r country codes.

    Found within a Road element.

    Parameters
    ----------
    s : float
        Start position (s-coordinate).
    type : str
        Country code of the road (see ISO 3166-1 alpha-2 codes).
    country : str
        Country code of the road (see ISO 3166-1 alpha-2 codes).

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    speed : RoadSpeed
        Object to define the maximum speed allowed.
    """
    def __init__(self, s=0, type="", country="") -> None:
        self.attrib = {
            "s": float(s),
            "type": str(type),
            "country": str(country)
        }
        self.speed = None
