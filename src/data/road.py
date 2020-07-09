class Road:
    def __init__(self, name = "", length = 0, id = 0, junction = 0, rule = "RHT"):
        self.name = ""
        self.id = int(id)
        self.length = float(length)
        self.junction = int(junction)
        self.rule = rule #if no rule provided, RHT is assumed
        self.predecessor = None
        self.successor = None
