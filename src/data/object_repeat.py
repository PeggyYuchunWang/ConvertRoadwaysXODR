class Object_Repeat:
    """
    Describes a repeated instance of an object. The attributes of
    the repeated object may be changed.

    Found within an Object element.
    
    Parameters
    ----------   
    s : float
        Start position (s-coordinate).
    length : float
        Length of the repeated area along the reference line
        in the s-direction.
    distance : float
        Distance between two instances of the object
    t_start : float
        Lateral offset of object's reference point at @s.
    t_end : float
        Lateral offset of object's reference point at
        @s + @length.
    height_start : float
        Height of the object at @s.
    height_end : float
        Height of the object at @s + @length.
    z_offset_start : float
        Z-Offset of the object at @s
    z_offset_end : float
        Z-Offset of the object at @s + @length
    width_start : float
        Width of the object at @s
    width_end : float
        Width of the object at @s + @length
    length_start : float
        Length of the object at @s
    length_end : float
        Length of the object at @s + @length
    radius_start : float
        Radius of the object at @s
    radius_end : float
        Radius of the object at @s + @length

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.  

  

    """
    def __init__(self, s = 0, length = 0, distance = 0, t_start = 0, t_end = 0,
                 height_start = 0, height_end = 0, z_offset_start = 0, 
                 z_offset_end = 0, width_start = 0, width_end = 0,
                 length_start = 0, length_end = 0, radius_start = 0,
                 radius_end = 0) -> None:        
        self.attrib = {
            "s" : float(s),
            "length" : float(length),
            "distance" : float(distance),
            "t_start" : float(t_start),
            "t_end" : float(t_end),
            "height_start" : float(height_start),
            "height_end" : float(height_end),
            "z_offset_start" : float(z_offset_start),
            "z_offset_end" : float(z_offset_end),
            "width_start" : float(width_start),
            "width_end" : float(width_end),
            "length_start" : float(length_start),
            "length_end" : float(length_end),
            "radius_start" : float(radius_start),
            "radius_end" : float(radius_end)          
        }
