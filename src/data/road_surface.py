class Road_Surface(Road):
    def __init__(
        self,
        file="",
        sStart=0,
        sEnd=0,
        orientation="same",
        mode="",
        purpose="",
        sOffset=0,
        tOffset=0,
        zOffset=0,
        zScale=0,
        hOffset=0
    ):
        self.file = str(file)
        self.sStart = float(sStart)
        self.sEnd = float(sEnd)
        self.orientation = str(orientation)  # default is same; opt. "opposite"
        self.mode = str(mode)
        self.purpose = str(purpose)
        self.sOffset = float(sOffset)
        self.tOffset = float(tOffset)
        self.zOffset = float(zOffset)
        self.zScale = float(zScale)
        self.hOffset = float(hOffset)
