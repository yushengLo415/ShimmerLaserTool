
class MetalSheet:

    def __init__(self, density, area, thickness):
        self._density = float(density)
        self._area = float(area)
        self._thickness = int(thickness)
        self._weight = 0

    def GetWeight(self):
        return self._weight
    
    def GetDensity(self):
        return self._density
    
    def GetArea(self):
        return self._area
    
    def GetThickness(self):
        return self._thickness
    
    def SetWeight(self, weight):
        self._weight = weight
    
    def SetDensity(self, density):
        self._density = density

    def SetArea(self, area):
        self._area = area
    
    def SetThickness(self, thickness):
        self._thickness = thickness
    