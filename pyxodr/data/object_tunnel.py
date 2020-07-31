class Object_Tunnel:
    """
    Details about a tunnel element. Valid for the complete cross section of a
    road.

    Found within an Objects element.

    Parameters
    ----------
    s : float
        Position (s-coordinate).
    length : float
        Length of the tunnel (in s-direction).
    id : str
        Unique ID within database.
    type : str
        Type of the tunnel. For values, see UML Model.
    name : str
        Name of the tunnel. May be chosen freely.
    lighting : int
        Degree of artificial tunnel lighting. Either 0 or 1.
    daylight : int
        Degree of daylight intruding the tunnel. Either 0 or 1.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(
        self,
        s=0,
        length=0,
        id="",
        type="",
        name="",
        lighting=0,
        daylight=0
    ) -> None:
        self.attrib = {
               "s": float(s),
               "length": float(length),
               "id": str(id),
               "type": str(type),
               "name": str(name),
               "lighting": int(lighting),
               "daylight": int(daylight)
        }
