class Objects:
    """
    Container for all objects along a road.

    Attributes
    ----------
    objects : list
        List of Object elements to define common 3D objects that influence a
        road.
    references : list
        List of Object_Reference elements to define links between
        objects and roads, signals or other objects.
    tunnels : list
        List of Object_Tunnel elements to define the tunnels.
    """
    def __init__(self) -> None:
        self.objects = []
        self.references = []
        self.tunnels = []
        self.bridges = []
