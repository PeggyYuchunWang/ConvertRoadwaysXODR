import src.data.abcd_base as abcd_base


class Poly3(abcd_base.ABCD_base):
    """
    Describes a part of the road's reference line as a cubic polynomial.
    The polynomial is decribed in the local u/v coordinate system of the
    starting point. The starting point is determined by the x, y and hdg
    variables of the parent Geometry element.

    Found within a Geometry element.

    Parameters
    ----------
    a : int
        Generic parameter a.
    b : int
        Generic parameter b.
    c : int
        Generic parameter c.
    d : int
        Generic parameter d.

    Attributes
    ----------
    attrib : dict
        Attributes dictionary for the parameters specified above.
    """
    def __init__(self, a=0, b=0, c=0, d=0) -> None:
        super().__init__(a, b, c, d)
