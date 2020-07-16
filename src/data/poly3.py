from abcd_base import ABCD_base

class Poly3(abcd_base):
    """
        Describes a part of the road's reference line as a cubic polynomial.
        The polynomial is decribed in the local u/v coordinate system of the starting point.
        The starting point is determined by the x, y and hdg variables of the 
        parent Geometry element.

        Found within a Geometry element.

        Parameters
        ----------
        curv_start : float
            Curvature at the start of the Spiral element.
        curv_end : float
            Curvature at the end of the Spiral element.

        Attributes
        ----------
        attrib : dict
            Attributes dictionary for the parameters specified above.
    """
    def __init__(self, a = 0, b = 0, c = 0, d = 0) -> None:
        abcd_base.__init__(self, a, b, c, d)