class JunctionPredecessorSuccessor:
    """
    Provides information the predecessor / successor road of a virtual
    connection.

    Found within a Connection element.

    Parameters
    ----------
    element_type : str
        Type of the linked element. Currently only "road" is supported.
    element_id : str
        ID of the linked element.
    element_s : float
        Alternative to contact_point for virtual junctions. Signifies that the
        connection occurs within the predecessor. Only can be used for element
        type "Road."
    element_dir: str
        For when element_s is in use. Indicates the direction on the
        predecessor from which the road is entered.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(
        self,
        element_type="",
        element_id="",
        element_s=0,
        element_dir=""
    ) -> None:
        self.attrib = {
            "element_type": str(element_type),
            "element_id": str(element_id),
            "element_s": float(element_s),
            "element_dir": str(element_dir)
        }
