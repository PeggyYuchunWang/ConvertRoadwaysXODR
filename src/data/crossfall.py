class Crossfall(abcd_base, Lateral_Profile):
    def __init__(self, side = "", s = 0, a = 0, b = 0, c = 0, d = 0):
        abcd_base.__init__(self, a, b, c, d)
        self.side = str(side)
        self.s = float(s)