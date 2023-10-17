
class LaserInfo:
    
    #key為厚度，value分為別黑鐵、白鐵、鋁切割長度/米的價格與打孔的價格
    #若孔徑 > 14mm，打孔的額外收費雙倍
    _laserCostDict = {
        "0":[0, 0, 0, 0],
        "1":[20, 40, 40, 2],
        "2":[20, 40, 40, 2],
        "3":[30, 60, 60, 2],
        "4":[40, 80, 80, 2],
        "5":[50, 100, 100, 3],
        "6":[60, 120, 120, 3],
        "8":[80, 160, 160, 4],
        "9":[90, 180, 180, 4],
        "10":[100, 200, 200, 4],
        "12":[120, 240, 240, 4],
        "16":[200, 400, 400, 6],
        "20":[300, 600, 600, 8]
    }

    def __init__(self):
        self._type = 0
        self._thickness = int(0)
        self._length = float(0)
        self._largeHolesCount = int(0)
        self._tinyHolesCount = int(0)
    
    def GetLength(self):
        return self._length
    
    def GetLargeHolesCount(self):
        return self._largeHolesCount

    def GetTinyHolesCount(self):
        return self._tinyHolesCount
    
    def GetPrice(self):
        linecost = self._length * self._laserCostDict[str(self._thickness)][self._type]
        largeHoleCost = 2 * self._largeHolesCount * self._laserCostDict[str(self._thickness)][3]
        tinyHoleCost = self._tinyHolesCount * self._laserCostDict[str(self._thickness)][3]
        return linecost + largeHoleCost + tinyHoleCost
    
    def SetType(self, type):
        self._type = type
    
    def SetThickness(self, thickness):
        self._thickness = thickness

    def SetLength(self, length):
        self._length = length
    
    def SetLargeHoleCount(self, largeHoleCount):
        self._largeHolesCount = largeHoleCount
    
    def SetTinyHoleCount(self, tinyHoleCount):
        self._tinyHolesCount = tinyHoleCount