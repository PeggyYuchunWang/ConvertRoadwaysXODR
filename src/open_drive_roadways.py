class OpenDriveRoadways:
    def __init__(self):
        self.header = None
        self.roads = {}
        self.junctions = {}

class Header:
    def __init__(self, revMajor = "", revMinor = "", version = "",
            date = "", north = "", south = "", east = "", west = "",
            vendor = ""):
        self.revMajor = revMajor
        self.revMinor = revMinor
        self.version = version
        self.date = date
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.vendor = vendor
        self.geoReference = None
        self.userData = None

    def newGeoReference(self, text=""):
        self.geoReference = GeoReference(text)

class GeoReference:
    def __init__(self, text = ""):
        self.text = text

class UserData:
    def __init__(self, vectorScene = None):
        self.vectorScene = vectorScene

class VectorScene:
    def __init__(self, program="", version=""):
        self.program = program
        self.version = version

class Road:
    def __init__(self, name = "", id = 0, length = 0, junction = 0):
        self.name = name
        self.id = id
        self.length = length
        self.junction = junction
        self.roadPredecessor = None
        self.roadSuccessor = None
        self.type_s = ""
        self.type_type = ""
        self.max_speed = ""
        self.speed_unit = ""
        self.planView = []
        self.elevationProfile = []
        self.lanes = None

class elementType:
    def __init__(self, type = "", id = "", contactPoint = None):
        self.type = type
        self.id = id
        self.contactPoint = contactPoint

class Geometry:
    def __init__(self, s = 0, x = 0, y = 0, hdg = 0, length = 0):
        self.s = s
        self.x = x
        self.y = y
        self.hdg = hdg
        self.length = length
        self.type = None

class Line:
    def __init__(self):
        pass

class Arc:
    def __init__(self, curvature = 0):
        self.curvature = curvature

class Elevation:
    def __init__(self, s=0, a=0, b=0, c=0, d=0):
        self.s = s
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class Width:
    def __init__(self, sOffset=0, a=0, b=0, c=0, d=0):
        self.sOffset = sOffset
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class RoadMark:
    def __init__(self, sOffset=0, type="", material="", laneChange=""):
        self.sOffset = sOffset
        self.type = type
        self.material = material
        self.laneChange = laneChange
        self.width = ""

class Lanes:
    def __init__(self):
        self.laneOffset = []
        self.laneSection = []

class LaneOffset:
    def __init__(self, s=0, a=0, b=0, c=0, d=0):
        self.s = s
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class LaneSection:
    def __init__(self, s=0):
        self.s = s
        self.left = []
        self.center = []
        self.right = []

class Lane:
    def __init__(self, id="", type="", level=""):
        self.id = id
        self.type = type
        self.level = level
        self.lanePredecessorId = ""
        self.laneSuccessorId = ""
        self.width = None
        self.roadMark = None
        self.travelDir = ""

class LaneLink:
    def __init__(self, linkfrom="", linkto=""):
        self.linkfrom = linkfrom
        self.linkto = linkto

class Connection:
    def __init__(self, id="", incomingRoad="", connectingRoad="", contactPoint=""):
        self.id = id
        self.incomingRoad = incomingRoad
        self.connectingRoad = connectingRoad
        self.contactPoint = contactPoint
        self.laneLink = None

class Junction:
    def __init__(self, id="", name=""):
        self.id = id
        self.name = name
        self.connections = []
