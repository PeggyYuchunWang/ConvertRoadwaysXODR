class Object:
    """
    Describes a common 3D object that influences a road by expanding, 
    delimiting and supplementing its course.
    
    Parameters
    ----------   
    type : ***COME BACK TO THIS***
            
    id : str
        Unique ID within database.
    s : float
        Object's origin (s-coordinate).
    t : float
        Object's origin (t-coordinate).
    z_offset : float
        Z-Offset of object's origin relative to the elevation 
        of the reference line. 
    valid_length : float 
        Length of validity along s-axis.
    orientation : str
        Determines the validity in the s-direction. Either "+"=valid in positive
        s-direction, "-"=valid in negative s-direction or "none"=valid in 
        both directions.
    subtype : str
        Variant of a type.
    dynamic : str
        Indicates whether the object is dynamic or static. Default is 
        "no"=static. 
    hdg : float
        Heading angle of hte object relative to road direction.
    name : str
        Name of the object. May be chosen freely.
    pitch : float
        Pitch angle relative to the x/y-plane.
    roll : foat
        Roll angle relative to the x/y-plane.
    height : float
        Height of the object's bounding box.
    length : float
        Length of the object's bounding box.
    width : float
        Width of the angular object's bounding box.
    radius : float
        Radius of the circular object's bounding box.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  
    repeats : list
        List of Object_Repeat elements that describe repeated instances
        of this object. The attributes of these repeated objects may be
        different from this original object.
    outlines : list
        List of Object_Outline elements that describe the outline of objects
        that describe a series of corner points.
    material : Object_Material
        Object to describe the material of the object.
    validity : Object_Validity
        Object to define the validity of the object for certain lanes.
    parking_space : Object_Parking_Space
        Object initialized if the object is of a special type: parking space.
    markings : list
        List of Object_Markings elements to allow for the description of the 
        appearance of an object via multiple marking elements.
    borders : list
        list of Object_Border elements to specify a border along certain outline points.

    

    """
    def __init__(self, type ="", id = "", s = 0, t = 0, z_offset = 0, 
                 valid_length = 0, orientation = "", subtype = "", 
                 dynamic = "no", hdg = 0, name = "", pitch = 0, 
                 roll = 0, height = 0,  length = 0, width = 0, radius = 0) -> None:        
        self.attrib = {
            "type" : str(type),
            "id" : str(id),
            "s" : float(s),
            "t" : float(t),
            "z_offset" : float(z_offset),
            "valid_length" : float(valid_length),
            "orientation" : str(orientation),
            "subtype" : str(subtype),
            "dynamic" : str(dynamic),
            "hdg" : float(hdg),
            "name" : str(name),
            "pitch" : float(pitch),
            "roll" : float(roll),
            "height" : float(height),
            "length" : float(length),
            "width" : float(width),
            "radius" : float(radius)
        }
        self.repeats = []
        self.outlines = []
        self.material = None
        self.validity = None
        self.parking_space = None
        self.markings = []
        self.borders = []
