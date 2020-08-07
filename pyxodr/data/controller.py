class Controller:
    """
    Provides a wrapper for the behaviour of a group of signals.

    Parameters
    ----------
    id : str
        Unique ID within database.
    sequence : float
        Sequence number (priority) of this controller with respect
        to other controllers of the same logical level.
    name : str
        Name of the controller. May be chosen freely.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    signal_control_records : list
        List of ControllerSignalControl element types.
    """
    def __init__(self, id="", sequence="", name="") -> None:
        self.attrib = {
            "id": str(id),
            "sequence": str(sequence),
            "name": str(name)
        }
        self.signal_control_records = []
