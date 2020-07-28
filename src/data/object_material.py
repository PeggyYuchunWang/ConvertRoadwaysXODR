class Object_Material:
    """
    Defines the material of an object.

    Found within an Object element.

    Parameters
    ----------
    surface : str
        Describes the surface material. See surface material codes.
    friction : float
        Fiction value, depending on application.
    roughness : float
        Roughness value, depending on application.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.

    """
    def __init__(self, surface="", friction=0, roughness=0) -> None:        
        self.attrib = {
            "surface": str(surface),
            "friction": float(friction),
            "roughness": float(roughness)            
        }
