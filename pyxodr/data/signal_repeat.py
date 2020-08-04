class SignalRepeat:
    """
    Offers the ability to copy signal information between signals by
    referencing the content. Represented in OpenDRIVE by a <signalReference>
    element. However, it was chosen to change the name to SignalRepeat to
    reduce confusion between this data type and a SignalReference element,
    which is also found in a Signal element.

    Found within a Signal element.

    Parameters
    ----------
    s : float
        Position (s-coordinate).
    t : float
        Position (t-coordinate).
    id : str
        Unique ID of the referenced signal within the database.
    orientation : str
        Determines the validity in the s-direction. Either "+"=valid in
        positive s-direction, "-"=valid in negative s-direction or "none"=valid
        in both directions.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, s=0, t=0, id="", orientation="") -> None:        
        self.attrib = {
            "s": float(s),
            "t": float(t),
            "id": str(id),
            "orientation": str(orientation)
        }
