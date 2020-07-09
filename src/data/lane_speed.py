"""
    Specific Lane_Speeds may be specified. Lane_Speed overrides Road_Speed limits.
    The center lane must have no speed limit.
    If there are multiple lane speed limit elements per lane section, the
    elements must be defined in ascending order.
"""

class Lane_Speed:
    def __init__(self, sOffset = 0, max_speed = 0, unit = ""):
        self.sOffset = float(sOffset)
        self.max = float(max_speed)
        self.unit = str(unit)