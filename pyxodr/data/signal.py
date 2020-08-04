class Signal:
    """
    Detailed information about a signal along a road.

    Found within a Road element.

    Parameters
    ----------
    id : str
        Unique ID within database.
    s : float
        Signal's origin (s-coordinate).
    t : float
        Signal's origin (t-coordinate).
    name : str
        Name of the signal. May be chosen freely.
    z_offset : float
        z-offset of signals's origin relative to the elevation of the reference
        line.
    dynamic : str
        Indicates whether the signal is dynamic or static. Default is
        "no"=static. 
    orientation : str
        Determines the validity in the s-direction. Either "+"=valid in
        positive s-direction, "-"=valid in negative s-direction or
        "none"=valid in both directions.
    country : str
        Country code of the road.
    country_revision : str
        Revision of a country's coding scheme for signals
    valid_length : float
        Length of validity along s-axis.
    type : str
        Type according to country code or "-1" or "none."
    subtype : str
        Variant of a type.
    value : float
        Value of the signal.
    unit : str
        Unit of @value.
    height : float
        Height of the object's bounding box.
    width : float
        Width of the angular object's bounding box.
    text : str
        Additional text associated with the signal.
    h_offset : float
        Heading offset of hte signal relative to @orientation.
    pitch : float
        Pitch angle relative to the x/y-plane.
    roll : foat
        Roll angle relative to the x/y-plane.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.
    validity_records : list
        List of SignalValidity elements that allow for default validity of a
        signal to be replaced with explicit validity information.
    dependency_records : list
        List of SignalDependency elements that allows a signal to control one
        or more other signals.
    references : list
        List of SignalReference elements that link a signal to a series of
        other elements.
    position_inertial : SignalPositionInertial
        Object to describe the physical position in inertial coordinates.
        Mutually exclusive with position_road.
    position_road: SignalPositionRoad
        Object to describe the physical position in road coordinates. Mutually
        exclusive with position_inertial.
    repeats : list
        List of SignalRepeat elements which allows the same type of signal to
        be reference by multiple roads.
    """
    def __init__(
        self,
        id="",
        s=0,
        t=0,
        name="",
        z_offset=0,
        dynamic="no",
        orientation="",
        country="",
        country_revision="",
        valid_length=0,
        type="",
        subtype="",
        value=0,
        unit="",
        height=0,
        width=0,
        text="",
        h_offset=0,
        pitch=0,
        roll=0
    ) -> None:
        self.attrib = {
            "id": str(id),
            "s": float(s),
            "t": float(t),
            "name": str(name),
            "z_offset": float(z_offset),
            "dynamic": str(dynamic),
            "orientation": str(orientation),
            "country": str(country),
            "country_revision": str(country_revision),
            "valid_length": float(valid_length),
            "type": str(type),
            "subtype": str(subtype),
            "value": float(value),
            "unit": str(unit),
            "height": float(height),
            "width": float(width),
            "text": str(text),
            "h_offset": h_offset,
            "pitch": float(pitch),
            "roll": float(roll),
        }
        self.validity_records = []
        self.dependency_records = []
        self.references = []
        self.position_inertial = None
        self.position_road = None
        self.repeats = []
