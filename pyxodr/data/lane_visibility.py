class Lane_Visibility:
    """
    Defines the visibility in four directions relative to the lane's direction.

    Found within a Lane element.

    Parameters
    ----------
    s_offset: float
        Start position (s-coordinate) relative to the position of the preceding
        Lane_Section element.
    forward : float
        Visibility in the forward direction.
    back : float
        Visibility in the back direction.
    left : float
        Visibility in the left direction.
    right : float
        Visibility in the right direction.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(
        self,
        s_offset=0,
        forward=0,
        back=0,
        left=0,
        right=0
    ) -> None:
        self.attrib = {
            "s_offset": float(s_offset),
            "forward": float(forward),
            "back": float(back),
            "left": float(left),
            "right": float(right)
        }
