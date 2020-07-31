class Object_Validity:
    """
    Defines an object's validity with respect to the ID of certain lanes.

    Found within an Object element.

    Parameters
    ----------
    from_lane : str
        Minimum ID of the lanes for which the object is valid.
    to_lane : str
        Maximum ID of the lanes for which the object is valid.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.

    """
    def __init__(self, from_lane="", to_lane="") -> None:        
        self.attrib = {
            "from_lane": str(from_lane),
            "to_lane": str(to_lane)
        }
