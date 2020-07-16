class ABCD_base:
    """
        Lower level base class with generic a, b, c, d elements.

        Parameters
        ----------
        a : int, float
            Generic parameter a.
        b : int, float
            Generic parameter b.
        c : int, float
            Generic parameter c.
        d : int, float
            Generic parameter d.

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
    """
    def __init__(self, a = 0, b = 0, c = 0, d = 0) -> None:
        self.attrib = {
            "a" : a,
            "b" : b,
            "c" : c,
            "d" : d
        }
        
    