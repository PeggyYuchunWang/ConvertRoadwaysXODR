class Offset:
    """
        An offset of the whole dataset may be applied to avoid large coordinates and
        enable inertial relocation and re-orientation of datasets.

        Found within the Header element.

        Parameters
        ----------
        x : float
            Value by which the dataset is translated for x
        y : float 
            Value by which the dataset is translated for y
        z : float 
            Value by which the dataset is translated for z
        hdg : float
            Value by which the dataset is rotated around the origin
    """
    def __init__(self, x = 0, y = 0, z = 0, hdg = 0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z) #x, y, z translation
        self.hdg = float(hdg) #rotation around new origin