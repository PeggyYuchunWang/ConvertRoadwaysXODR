class ObjectBorder:
    """
    Defines the border of an object.

    Found within an Object element.

    Parameters
    ----------
    width : float
        Width of the border.
    type : str
        Appearance of the border. For values, see UML Model.
    outline_id : str
        ID of the outline to use.
    use_complete_outline : bool
        Use all outline points for border. Default is True.

    Attributes
    ----------
    attrib : dict
         Attributes dictionary for the parameters specified above.

    """
    def __init__(
        self,
        width=0,
        type="",
        outline_id="",
        use_complete_outline=True
    ) -> None:        
        self.attrib = {
            "width": float(width),
            "type": str(type),
            "outline_id": str(outline_id),
            "use_complete_outline": bool(use_complete_outline)  
        }
