class ObjectOutlineCornerLocal:
    """
    Describes non-linear forms of objects. Mutually exclusive with
    ObjectOutlineCornerRoad elements.

    Found within an ObjectOutline element.

    Parameters
    ----------
    id : str
        ID of the corner. Unique within on ObjectOutline element.
    u : float
        Local u-coordinate of the corner.
    v : float
        Local v-coordinate of the corner.
    z : float
        Local z-coordinate of the corner.
    height : float
        Height of the object at this corner along the z-axis.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, id="", u=0, v=0, z=0, height=0) -> None:   
        self.attrib = {
            "id": str(id),
            "u": float(u),
            "v": float(v),
            "z": float(z),
            "height": float(height)           
        }
