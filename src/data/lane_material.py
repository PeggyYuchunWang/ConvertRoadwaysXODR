class Lane_Material:
    """
    Defines the surface, friction and roughness of the material of a lane.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        Lane_Section element.
    friction : float
        Friction value.
    surface : str
        Surface material code.
    roughness : float
        Roughness for sound and motion systems.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(
        self,
        s_offset=0,
        friction=0,
        surface="",
        roughness=0
    ) -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "friction": float(friction),
            "surface": str(surface),
            "roughness": float(roughness)
        }
