class ObjectParkingSpace:
    """
    Details for a parking space object.

    Found within an Object element.

    Parameters
    ----------
    access : str
        Defines the access rule for the parking space. For all possible values,
        see UML Model.
    restrictions : str
        Free text, depending on application.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    """
    def __init__(self, access="all", restrictions="") -> None:
        self.attrib = {
               "access": str(access),
               "restrictions": str(restrictions)
        }
