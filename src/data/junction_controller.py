class Junction_Controller:
    """
    Lists the controllers that are used for the management
    of a junction.

    Found within a Junction element.

    Parameters
    ----------
    id : str
        Unique ID given to the group, stored within the database.
    type : str
        Type of control. Depends on application.
    sequence : int
        Sequence number of this controller with respect to the other
        controllers in the same junction.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, id="", type="", sequence=0) -> None:
        self.attrib = {
            "id": str(id),            
            "type": str(type),
            "sequence": int(sequence)
        }
