class Signal_Position_Inertial:
    """
    Describes the reference point of the physical position in inertial
    coordinates in cases where it deviates from the logical position.

    Found within a Signal element.

    Parameters
    ----------
    x : float
        Posiition (x-coordinate).
    y : float
        Posiition (y-coordinate).
    z : float
        Posiition (z-coordinate).
    hdg : float
        Heading of the signal.
    pitch : float
        Pitch angle of the signal after applying the heading.
    roll : float
        Roll angle of the signal after applying heading and pitch.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, x=0, y=0, z=0, hdg=0, pitch=0, roll=0) -> None:
        self.attrib = {
            "x": float(x),
            "y": float(y),
            "z": float(z),
            "hdg": float(hdg),
            "pitch": float(pitch),
            "roll": float(roll)
        }
