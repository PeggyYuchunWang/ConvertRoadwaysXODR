class Geo_Reference:
    """
        Information about the geographic reference for an OpenDRIVE dataset.
        Found within the Header element.
    """
    def __init__(self, text = ""):
        self.text = text