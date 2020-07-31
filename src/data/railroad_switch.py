class Railroad_Switch:
    """
    Allows rail-bound vehicles to change tracks.

    Found within a Railroad element.

    Parameters
    ----------
    name : str
        Unique name of the switch.
    id : str
        Unique ID of the switch.
    position : str
        Defines if the swtich can be operated (dynamic).
        or it is in a static position. For value, see UML Model.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    main_track : Railroad_Track
    side_track : Railroad_Track
    switch_partnet : Railroad_Switch_Partner
    """
    def __init__(self, name="", id="", position="") -> None:
        self.attrib = {
            "name": str(name),
            "id": str(id),
            "position": str(position)
        }
        self.main_track = None
        self.side_track = None
        self.switch_partner = None
