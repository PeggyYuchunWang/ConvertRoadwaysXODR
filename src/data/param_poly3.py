"""
    Allows for the generation of road courses with parametric cubic curves.
    They may be caculated simultaneously using local u- and v-coordinates:
    u(p) = aU  + bU*p + cU*p^2 + dU*p^3
    v(p) = aV + bV*p + cv*p^2 + dV*p^3
"""
import Geometry

class Param_Poly3(Geometry):
    def __init__(self, aU=0, bU=0, cU=0, dU=0, aV=0, bV=0, cV=0, dV=0, pRange=""):
        self.aU = float(aU)
        self.bU = float(bU)
        self.cU = float(cU)
        self.dU = float(dU)
        self.aV = float(aV)
        self.bV = float(bV)
        self.cV = float(cV)
        self.dV = float(dV)
        self.pRange = pRange