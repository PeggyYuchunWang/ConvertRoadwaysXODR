#from src.data.abcd_base import abcd_base
#from src.data.arc import Arc
#from src.data.crossfall import Crossfall
from src.data.header import Header
from src.data.geo_reference import Geo_Reference
from src.data.offset import Offset
from src.data.road import Road

class Open_Drive_Framework:
    """
        Compilation of all Open Drive elements information in an object oriented framework.
    """
    def __init__(self):
        self.header = None
        self.roads = {}
        self.junctions = {}

    # def Header(self, revMajor = 0, revMinor = 0, name = "", version = "",
    #         date = "", north = 0, south = 0, east = 0, west = 0):
    #     return Header(revMajor, revMinor, name, version, date, north, south, east, west)

    # def _Geo_Reference(self, text = ""):
    #     return Geo_Reference(text)

    # def _Offset(self, x = 0, y = 0, z = 0, hdg = 0):
    #     return Offset(x, y, z, hdg)

    # def _Road(self, name = "", length = 0, id = 0, junction = 0, rule = "RHT"):
    #     self.roads[id] = Road(name, length, id, junction, rule)