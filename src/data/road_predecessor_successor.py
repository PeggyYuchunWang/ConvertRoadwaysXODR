class Road_Predecessor_Successor:
    def __init__(self, id = 0, type = "", contact_point = "", element_s = None, element_dir = 0):
        self.id = int(id)
        self.type = type #road or junction
        self.contact_point = contact_point #eiher start for predecessor, or end for successor
        self.element_s = element_s #only for virtual junctions, AKA contact_point is not at start or end
        self.element_dir = element_dir #only for virtual junctions
