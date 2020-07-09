class Lane_Material:
    def __init__(self, sOffset = 0, surface = "", friction = 0, roughness = 0):
        self.sOffset = float(sOffset)
        self.surface = str(surface)
        self.friction = float(friction)
        self.roughness = float(roughness)
