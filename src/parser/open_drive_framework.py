#from src.data.abcd_base import abcd_base
#from src.data.arc import Arc
#from src.data.crossfall import Crossfall
import src.data.header as header
import src.data.geo_reference as geo_reference
import src.data.offset as offset
import src.data.road as road

class Open_Drive_Framework:
    """
        Compilation of all Open Drive elements information in an object oriented framework.
    """
    def __init__(self):
        self.header = None
        self.geo_reference = None
        self.offset = None
        self.roads = {}
        self.junctions = {}

    def Header(self, revMajor = 0, revMinor = 0, name = "", version = "",
            date = "", north = 0, south = 0, east = 0, west = 0):
        return header.Header(revMajor, revMinor, name, version, date, north, south, east, west)

    def Geo_Reference(self, text = ""):
        return geo_reference.Geo_Reference(text)

    def Offset(self, x = 0, y = 0, z = 0, hdg = 0):
        return offset.Offset(x, y, z, hdg)