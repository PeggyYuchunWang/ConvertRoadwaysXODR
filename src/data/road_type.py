"""
    Valid for the entire cross section of a road, until a new road type element
    is provided or until the road ends. Country code and state identifier may be added
    to the <type> element to specify national traffic rules. This will not
    be specified by OpenDRIVE. Only use ALPHA-r country codes.
"""

import Road

class Road_Type(Road):
    def __init__(self, s = 0, type = 0, country = 0):
        self.s = float(s)
        self.type = float(type)
        self.country = float(country)