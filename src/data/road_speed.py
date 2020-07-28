class Road_Speed:
    """
        Defines the maximum speed allowed on a road.

        Found within a Road_Type element.

        Parameters
        ----------
        max : str, float
            Maximum allowed speed. Either a string "no limit" or "undefined,"
            or a numerical value.
        unit : str
            Unit of the max speed parameter.

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
    """
    def __init__(self, max=None, unit="") -> None:
        self.attrib = {
            "max": None,
            "unit": str(unit)
        }
