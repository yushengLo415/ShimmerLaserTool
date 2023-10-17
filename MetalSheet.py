
class MetalSheet:

    def __init__(self):
        self._density = float(0.00000785)
        self._area = float(0)
        self._thickness = int(0)
        self._unitPrice = int(0)

    def GetArea(self):
        return self._area
    
    def GetThickness(self):
        return self._thickness
    
    def GetUnitPrice(self):
        return self._unitPrice

    def GetWeight(self):
        return self._area * self._thickness * self._density

    def GetPrice(self):
        return self._area * self._thickness * self._density * self._unitPrice
    
    def SetType(self, type):
        if type == 0:
            self._density = 0.00000785
        elif type == 1:
            self._density = 0.00000793
        elif type == 2:
            self._density = 0.00000271

    def SetArea(self, area):
        self._area = area
    
    def SetThickness(self, thickness):
        self._thickness = thickness
    
    def SetUnitPrice(self, unitPrice):
        self._unitPrice = unitPrice
