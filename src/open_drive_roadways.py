class OpenDriveRoadways:
    def __init__(self):
        self.header = None
        self.roads = {}
        self.junctions = {}

class Header:
    def __init__(self, revMajor = 0, revMinor = 0, name = "", version = "",
            date = "", north = 0, south = 0, east = 0, west = 0):
        self.revMajor = int(revMajor)
        self.revMinor = int(revMinor)
        self.name = name
        self.version = version
        self.date = date
        self.north = float(north)
        self.south = float(south)
        self.east = float(east)
        self.west = float(west)
        self.vendor = ""
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
    def __init__(self, id = 0, length = 0, junction = 0):
        self.name = ""
        self.id = int(id)
        self.length = float(length)
        self.junction = int(junction)
        self.roadPredecessor = None
        self.roadSuccessor = None
        self.type_s = 0
        self.type_type = ""
        self.max_speed = 0
        self.speed_unit = ""
        self.planView = []
        self.elevationProfile = []
        self.lanes = None

class elementType:
    def __init__(self, type = "", id = 0, contactPoint = None):
        self.type = type
        self.id = int(id)
        self.contactPoint = contactPoint

class Geometry:
    def __init__(self, s = 0, x = 0, y = 0, hdg = 0, length = 0):
        self.s = float(s)
        self.x = float(x)
        self.y = float(y)
        self.hdg = float(hdg)
        self.length = float(length)
        self.type = None

class Line:
    def __init__(self):
        pass

class Arc:
    def __init__(self, curvature = 0):
        self.curvature = float(curvature)

class Spiral:
    def __init__(self, curveStart=0, curveEnd=0):
        self.curveStart = curveStart
        self.curveEnd = curveEnd

class Poly3:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

class ParamPoly3:
    def __init__(self, pRange="", aU=0, bU=0, cU=0, dU=0, aV=0, bV=0, cV=0, dV=0):
        self.pRange = pRange
        self.aU = float(aU)
        self.bU = float(bU)
        self.cU = float(cU)
        self.dU = float(dU)
        self.aV = float(aV)
        self.bV = float(bV)
        self.cV = float(cV)
        self.dV = float(dV)

class Elevation:
    def __init__(self, s=0, a=0, b=0, c=0, d=0):
        self.s = float(s)
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

class Width:
    def __init__(self, sOffset=0, a=0, b=0, c=0, d=0):
        self.sOffset = float(sOffset)
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

class RoadMark:
    def __init__(self, sOffset=0, type="", laneChange=""):
        self.sOffset = float(sOffset)
        self.type = type
        self.material = ""
        self.laneChange = laneChange
        self.width = 0

class Lanes:
    def __init__(self):
        self.laneOffset = []
        self.laneSection = []

class LaneOffset:
    def __init__(self, s=0, a=0, b=0, c=0, d=0):
        self.s = float(s)
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

class LaneSection:
    def __init__(self, s=0):
        self.s = float(s)
        self.single_side = False
        self.left = {}
        self.center = {}
        self.right = {}

class Lane:
    def __init__(self, id=0, type="", level=False):
        self.id = int(id)
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
    def __init__(self, id=""):
        self.id = id
        self.type = "default"
        self.incomingRoad = ""
        self.connectingRoad = ""
        self.contactPoint = ""
        self.laneLink = None

class Junction:
    def __init__(self, id="", name=""):
        self.id = id
        self.name = name
        self.type = "default"
        self.connections = []
