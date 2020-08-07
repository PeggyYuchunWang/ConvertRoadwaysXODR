class RoadMarkExplicit:
    """
    Detailed information about irregular road markings that cannot be described
    by repetitive line patterns.

    Found within a RoadMark element.

    Parameters
    ----------
    name : str
        Name of the road mark type. May be chosen freely.
    width : float
        Accumulated width of the road mark. If there are several line elements,
        width is the sum of all line specific width elements.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    lines : list
        List of line elements that describe the road marking type.
    """
    def __init__(self, name="", width=0) -> None:
        self.attrib = {
            "name": str(name),
            "width": float(width)
        }
        self.lines = []
