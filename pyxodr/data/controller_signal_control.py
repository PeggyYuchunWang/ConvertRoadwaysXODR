class ControllerSignalControl:
    """
    Provides information about a single signal controlled by corresponding
    controller.

    Found within a Controller element.

    Parameters
    ----------
    signal_id : str
        ID of the controlled signal.
    type : str
        Type of control. Free text, depending on application.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, signal_id="", type="") -> None:
        self.attrib = {
            "signal_id": str(signal_id),
            "type": str(type)
        }
