class Road_Mark_Line:
    """
    Information on the road mark line.

    Found within a Road_Mark_Type element.

    Parameters
    ----------
    length : float
        Length of the visible part of the line.
    space : float
        Length of the gap between the visible parts.
    t_offset : float
        Lateral offset from the lane border.
    s_offset : float
        Initial longitudinal offset of the line definition 
        from the start of the road mark definition.
    rule : str
        Rule that must be observed when passing the line from inside. 
        Either "no passiong," "caution," or "none."
    width : float
        Width of the line.
    color : str
        Color of the line.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, length = 0, space = 0, t_offset = 0, s_offset = 0, rule = "", width = 0, color = "") -> None:
        self.attrib = {
            "length" : float(length),
            "space" : float(space),
            "t_offset" : float(t_offset),
            "s_offset" : float(s_offset),
            "rule" : str(rule),
            "width" : float(width),
            "color" : str(color)
        }