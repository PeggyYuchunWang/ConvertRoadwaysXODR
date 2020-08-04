class ObjectOutlineCornerRoad:
    """
    Decribes non-linear forms of an objects. Mutually exclusive with
    ObjectOutlineCornerLocal elements.

    Found within an ObjectOutline element.

    Parameters
    ----------
    id : str
        ID of the corner. Unique within on ObjectOutline element.
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
