class Station:
    """
    Defines a station for tram and railroad applications and for automotive
    environments.

    Parameters
    ----------
    id : str
        Unique ID within the database.
    name : str
        Name of the station. May be chosen freely.
    type : str
        Type of the station. Free text, depending on application.
        Either "small," "medium," or "large."

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    platforms : list
        List of Station_Platform elements that describe the platforms that make
        up the specified station.
    """
    def __init__(
        self,
        id="",
        name="",
        type=""
    ) -> None:
        self.attrib = {
            "id": str(id),
            "name": str(name),
            "type": str(type)
        }
        self.platforms = []
