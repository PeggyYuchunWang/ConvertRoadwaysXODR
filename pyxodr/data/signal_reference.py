class SignalReference:
    """
    Provides a mean to link a signal to a series of other elements.

    Found within a Signal element.

    Parameters
    ----------
    element_type : str
        Type of the linked element.
    element_id : str
        Unique ID of the linked element.
    type : str
        Type of the linkage.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, element_type="", element_id="", type="") -> None:
        self.attrib = {
            "element_type": str(element_type),
            "element_id": str(element_id),
            "type": str(type)
        }
