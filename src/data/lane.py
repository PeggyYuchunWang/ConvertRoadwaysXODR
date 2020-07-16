"""
    Basic class for Lane creation. Left Lanes must have negative id values, Right Lanes 
    must have positive id values and Center Lanes have an id value of 0.

    If linkage between lanes is ambiguous, junctions must be used. Otherwise, specify
    the predecessor / successor for the Lane.

    The Lane type defines the main purpose of a lane and its corresponding traffic rules.
"""

class Lane:
    def __init__(self, id = 0):
        self.id = int(id)
        self.predecessor_id = None #another Lane type with an id
        self.successor_id = None #another Lane type with an id
        self.type = None
        self.level = False #default --> apply superelevation
        self.lane_material = None



