class Object_Outline_Corner_Road:
    """
    Decribes non-linear forms of an objects. Mutually exclusive with
    Object_Outline_Corner_Local elements.

    Found within an Object_Outline element.

    Parameters
    ----------
    id : str
        ID of the corner. Unique within on Object_Outline element.
    s : float
        s-coordinate of the corner.
    t : float
        t-coordinate of the corner.
    dz : float
        dz of the corner relative to the road reference line.
    height : float
        Height of the object at this corner along the z-axis

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, id="", s=0, t=0, dz=0, height=0) -> None:
        self.attrib = {
            "id": str(id),
            "s": float(s),
            "t": float(t),
            "dz": float(dz),
            "height": float(height)
        }
