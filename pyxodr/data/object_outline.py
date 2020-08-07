class ObjectOutline:
    """
    Defines an outline of objects that describe a series of corner points,
    mainly used to describe traffic islands, irregularly shaped parking spaces
    and special road markings.

    Found within an Object element.

    Parameters
    ----------
    id : str
        ID of the outline. Unique within on object.
    fill_type : str
        Type used to fill the area inside the outline. For values, see UML
        Model.
    outer : bool
        Defines if the outline is an outer outline of the object.
    closed : bool
        Defines if the outline describes an area, not a linear feature.
    lane_type : str
        Type used to describe the lane typ eof hte outline. For values,
        see UML Model.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    corner_roads : list
        List of ObjectOutlineCornerRoad elements that describe non-linear
        forms of objects. Mutually exclusive with corner_locals.
    corner_locals : list
        List of ObjectOutlineCornerLocal elements that describe non-linear
        forms of objects. Mutually exclusive with corner_roads.

    """
    def __init__(
        self,
        id="",
        fill_type="",
        outer=True,
        closed=False,
        lane_type=""
    ) -> None:
        self.attrib = {
            "id": str(id),
            "fill_type": str(fill_type),
            "outer": bool(outer),
            "closed": bool(closed),
            "lane_type": str(lane_type),
        }
        self.corner_roads = []
        self.corner_locals = []
